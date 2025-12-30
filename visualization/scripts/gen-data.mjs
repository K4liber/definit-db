import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');
const indexPath = path.resolve(repoRoot, '../src/definit_db/data_md/index.md');
const defsRoot = path.resolve(repoRoot, '../src/definit_db/data_md/definitions');
const outPath = path.resolve(repoRoot, './public/defs.json');

function normalizeId(s) {
  return s
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '_')
    .replace(/[^a-z0-9_\-]/g, '');
}

function parseIndex(md) {
  // lines like: - [object](mathematics/fundamental/object)
  const items = [];
  const re = /^-\s+\[([^\]]+)\]\(([^)]+)\)\s*$/;

  for (const line of md.split(/\r?\n/)) {
    const m = re.exec(line.trim());
    if (!m) continue;
    const title = m[1];
    const relPath = m[2].replace(/\.md$/i, '');

    // Use relPath as the stable, human-readable unique id.
    // Example: "computer_science/foundamental/bit"
    const id = relPath;

    const filePath = path.resolve(defsRoot, `${relPath}.md`);
    items.push({ id, title, relPath, filePath });
  }
  return items;
}

async function readIfExists(p) {
  try {
    return await fs.readFile(p, 'utf8');
  } catch {
    return null;
  }
}

function normalizeHrefToIndexRelPath(href, ctx, idByRelPath) {
  const clean = String(href ?? '').trim();
  if (!clean) return null;
  if (clean.startsWith('#')) return null;

  // strip anchors/query
  const noHash = clean.split('#')[0].split('?')[0];

  // ignore external urls
  if (/^[a-z]+:\/\//i.test(noHash)) return null;

  // remove leading ./ and trailing .md
  const p = noHash.replace(/^\.\//, '').replace(/\.md$/i, '');
  if (!p.includes('/')) return null;

  // Exact match
  if (idByRelPath.has(p)) return p;

  // Shorthand: "field/definition" where index uses deeper paths like
  // "field/<subtree>/definition".
  // Resolve by looking for an index relPath that ends with "/definition" *within the same field*.
  const parts = p.split('/');
  const field = parts[0];
  const last = parts.at(-1);
  if (!field || !last) return null;

  const suffix = `/${last}`;

  const matches = [];
  for (const rel of idByRelPath.keys()) {
    if (rel.startsWith(`${field}/`) && rel.endsWith(suffix)) matches.push(rel);
  }

  if (matches.length === 1) return matches[0];

  return null; // ambiguous or not found
}

function extractDeps(md, ctx, idByRelPath, stats) {
  // Heuristic: dependencies are written inside definitions content.
  // Pattern: [label](some/path) - we take label as a candidate dependency id
  //
  // Notes:
  // - We try hard to ignore self-references and non-dependency links.

  const deps = new Set();

  const isSelf = (candidateId, href) => {
    if (!candidateId) return false;
    if (candidateId === ctx.id) return true;

    if (href) {
      const clean = String(href).trim();
      if (!clean) return false;
      if (clean === ctx.relPath || clean === `${ctx.relPath}.md`) return true;
      if (clean === `./${ctx.relPath}` || clean === `./${ctx.relPath}.md`) return true;
      if (clean.endsWith(`#${ctx.id}`) || clean === `#${ctx.id}`) return true;
    }

    return false;
  };

  const linkRe = /\[([^\]]+)\]\(([^)]+)\)/g;
  for (const m of md.matchAll(linkRe)) {
    const label = m[1];
    const href = (m[2] ?? '').trim();

    const rel = normalizeHrefToIndexRelPath(href, ctx, idByRelPath);
    if (rel) {
      const depId = idByRelPath.get(rel);
      if (depId && !isSelf(depId, href)) deps.add(depId);
      continue;
    }

    // Track unresolved/ambiguous href-based refs (useful to tune parsing).
    if (href && href.includes('/') && !href.startsWith('#') && !/^[a-z]+:\/\//i.test(href)) {
      stats.unresolvedHref++;
    }

    // Fallback: label-based (not unique across fields)
    const labelId = normalizeId(label);
    if (labelId && !isSelf(labelId, href)) deps.add(labelId);
  }

  return [...deps].filter(Boolean);
}

function computeLevels(nodes) {
  // Kept for cycle detection + dep filtering; UI computes levels dynamically.
  const byId = new Map(nodes.map((n) => [n.id, n]));

  // keep only deps that exist in index
  for (const n of nodes) {
    n.deps = n.deps.filter((d) => d && byId.has(d) && d !== n.id);
  }

  // DFS to detect cycles; we also compute a temporary level to preserve previous validation behavior.
  const visiting = new Set();
  const visited = new Set();
  const stack = [];

  function formatNode(id) {
    const n = byId.get(id);
    if (!n) return id;
    return `${n.id} (${n.relPath})`;
  }

  function dfs(id) {
    if (visited.has(id)) return byId.get(id).level;

    if (visiting.has(id)) {
      const start = stack.indexOf(id);
      const cycleIds = start >= 0 ? stack.slice(start).concat(id) : [id, id];
      const cyclePretty = cycleIds.map(formatNode).join(' -> ');

      const hopDetails = [];
      for (let i = 0; i < cycleIds.length - 1; i++) {
        const a = cycleIds[i];
        const b = cycleIds[i + 1];
        const an = byId.get(a);
        hopDetails.push(`${formatNode(a)} depends on ${formatNode(b)} (deps: ${an?.deps?.length ?? 0})`);
      }

      console.error('\nCYCLE DETECTED');
      console.error(cyclePretty);
      console.error('\nHOPS');
      for (const line of hopDetails) console.error(`- ${line}`);
      console.error('');

      throw new Error(`Cycle detected involving ${id}`);
    }

    visiting.add(id);
    stack.push(id);

    const n = byId.get(id);
    let lvl = 0;
    for (const dep of n.deps) {
      lvl = Math.max(lvl, dfs(dep) + 1);
    }
    n.level = lvl;

    stack.pop();
    visiting.delete(id);
    visited.add(id);

    return lvl;
  }

  for (const n of nodes) dfs(n.id);
}

async function main() {
  const indexMd = await fs.readFile(indexPath, 'utf8');
  const items = parseIndex(indexMd);

  // map relPath -> id for dependency resolution
  const idByRelPath = new Map(items.map((it) => [it.relPath.replace(/\.md$/i, ''), it.id]));

  const nodes = [];
  let missingFiles = 0;
  const stats = { unresolvedHref: 0 };

  for (const it of items) {
    const md = await readIfExists(it.filePath);
    if (!md) missingFiles++;
    const deps = md ? extractDeps(md, it, idByRelPath, stats) : [];
    nodes.push({ ...it, deps, level: 0, content: md || '' });
  }

  // Validate deps and detect cycles (also assigns temporary levels on nodes).
  computeLevels(nodes);

  const edges = [];
  for (const n of nodes) {
    for (const dep of n.deps) edges.push({ source: n.id, target: dep });
  }

  const graph = { nodes, edges };
  await fs.mkdir(path.dirname(outPath), { recursive: true });
  await fs.writeFile(outPath, JSON.stringify(graph, null, 2), 'utf8');
  console.log(
    `Wrote ${outPath} (nodes=${nodes.length}, edges=${edges.length}, missingFiles=${missingFiles}, unresolvedHref=${stats.unresolvedHref})`
  );
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
