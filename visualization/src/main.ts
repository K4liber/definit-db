import * as d3 from 'd3';
import type { DefGraph, DefNode, NodeKind } from './types';

const svg = d3.select<SVGSVGElement, unknown>('#viz');

const W = () => svg.node()!.clientWidth;
const H = () => svg.node()!.clientHeight;

const gRoot = svg.append('g');
const gRings = gRoot.append('g').attr('class', 'rings');
const gLinks = gRoot.append('g').attr('class', 'links');
const gNodes = gRoot.append('g').attr('class', 'nodes');

const zoom = d3
  .zoom<SVGSVGElement, unknown>()
  .scaleExtent([0.1, 6])
  .on('zoom', (ev: d3.D3ZoomEvent<SVGSVGElement, unknown>) => {
    gRoot.attr('transform', ev.transform.toString());
  });

svg.call(zoom as any);

function colorForLevel(level: number) {
  return level === 0 ? '#38bdf8' : d3.interpolateRainbow(Math.min(1, level / 20));
}

function normalizeId(s: string) {
  return s
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '_')
    .replace(/[^a-z0-9_\-\/]/g, '');
}

function setStats(graph: DefGraph) {
  const maxLevel = Math.max(0, ...graph.nodes.map((n) => n.level ?? 0));

  const statsEl = document.getElementById('stats')!;
  statsEl.innerHTML = '';
  const kv: Array<[string, string]> = [
    ['Nodes', String(graph.nodes.length)],
    ['Edges', String(graph.edges.length)],
    ['Levels', String(maxLevel + 1)],
    ['Max level', String(maxLevel)],
  ];
  for (const [k, v] of kv) {
    const dk = document.createElement('div');
    dk.textContent = k;
    const dv = document.createElement('div');
    dv.textContent = v;
    statsEl.appendChild(dk);
    statsEl.appendChild(dv);
  }
}

type Pos = { x: number; y: number };

// keep track of which level ring is currently highlighted
let hoveredLevel: number | null = null;

// keep track of which node is selected for ring focus
let selectedNodeId: string | null = null;

function applyRingHighlight() {
  // Hover ring takes precedence; otherwise fall back to selected node ring.
  let level: number | null = hoveredLevel;

  if (level === null && selectedNodeId && lastProjected) {
    const n = lastProjected.nodes.find((x) => x.id === selectedNodeId);
    level = n?.level ?? null;
  }

  gRings
    .selectAll<SVGCircleElement, { level: number; r: number }>('circle.ring')
    .classed('hovered', (d) => level !== null && d.level === level);
}

function setRingHighlight(level: number | null) {
  hoveredLevel = level;
  applyRingHighlight();
}

function textWidthPx(text: string) {
  // rough estimate (panel uses ~12-13px font sizes)
  return Math.max(24, text.length * 7.2);
}

function hash01(s: string) {
  // deterministic 0..1
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return (h >>> 0) / 0xffffffff;
}

function fieldOfId(id: string) {
  if (id.startsWith('field:')) return id.slice('field:'.length);
  if (id.startsWith('cat:')) {
    const rest = id.slice('cat:'.length);
    return rest.split('/')[0] ?? rest;
  }
  return id.split('/')[0] ?? id;
}

// Learning-state coloring (Definitions mode)
const COLOR_OFF = 'rgba(148, 163, 184, 0.18)'; // barely visible
const COLOR_VISIBLE = 'rgba(148, 163, 184, 0.8)'; // normal grey
const COLOR_READY = '#fbbf24'; // yellow
const COLOR_LEARNED = '#22c55e'; // green

type LearnState = 'off' | 'visible' | 'ready' | 'learned';

const LEARNED_STORAGE_KEY = 'definit-db.learned';

function loadLearnedFromStorage() {
  try {
    const raw = localStorage.getItem(LEARNED_STORAGE_KEY);
    if (!raw) return new Set<string>();
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return new Set<string>();
    return new Set<string>(arr.filter((x) => typeof x === 'string'));
  } catch {
    return new Set<string>();
  }
}

function saveLearnedToStorage() {
  try {
    localStorage.setItem(LEARNED_STORAGE_KEY, JSON.stringify(Array.from(learned)));
  } catch {
    // ignore
  }
}

function clearLearnedProgress() {
  learned.clear();
  try {
    localStorage.removeItem(LEARNED_STORAGE_KEY);
  } catch {
    // ignore
  }
}

const learned = loadLearnedFromStorage();

function learnStateForNode(n: DefNode): LearnState {
  // Base state from learning/progression only.
  // Only leaves exist in Definitions mode; treat anything else as off.
  if (n.kind !== 'leaf') return 'off';
  if (learned.has(n.id)) return 'learned';

  // Ready if all deps are learned (including "no deps").
  const deps = n.deps ?? [];
  const allLearned = deps.every((d) => learned.has(d));
  if (allLearned) return 'ready';

  return 'off';
}

function colorForLearnState(s: LearnState) {
  if (s === 'learned') return COLOR_LEARNED;
  if (s === 'ready') return COLOR_READY;
  if (s === 'visible') return COLOR_VISIBLE;
  return COLOR_OFF;
}

// Cache the most recent layout used for rendering so zoom-to-ring uses the same geometry.
let lastLayout: ReturnType<typeof radialLayout> | null = null;

function radialLayout(graph: DefGraph) {
  const width = W();
  const height = H();
  const cx = width / 2;
  const cy = height / 2;

  const maxLevel = Math.max(0, ...graph.nodes.map((n) => n.level ?? 0));

  // Make rings less dense for large labels.
  const maxLabel = Math.max(6, ...graph.nodes.map((n) => n.title?.length ?? 0));
  const ringGap = Math.max(54, Math.min(120, 30 + maxLabel * 2.4));
  const base = 56;

  const byLevel = d3.group(graph.nodes, (n: DefNode) => n.level ?? 0);

  const placed = new Map<string, Pos>();

  // Per-level angular offset so nodes on different rings don't align.
  const levelOffset = (level: number) => (hash01(String(level)) * 0.9 + level * 0.37) % (Math.PI * 2);

  // Simple per-ring relaxation in angle space to reduce overlaps.
  // We treat each node as needing an arc length proportional to its label width.
  const relaxAngles = (nodes: DefNode[], r: number, baseAngles: number[]) => {
    if (nodes.length <= 1) return baseAngles;

    const angles = baseAngles.slice();
    const widths = nodes.map((n) => textWidthPx(n.title));

    // Convert desired pixel spacing into angular spacing.
    const need = widths.map((w) => (w + 18) / Math.max(1, r));

    // iteration: push neighbors apart
    const iters = 22;
    for (let it = 0; it < iters; it++) {
      // sort by angle
      const idx = d3.range(nodes.length).sort((a, b) => angles[a] - angles[b]);
      for (let j = 0; j < idx.length; j++) {
        const a = idx[j];
        const b = idx[(j + 1) % idx.length];

        // circular distance
        let da = angles[b] - angles[a];
        if (da < 0) da += Math.PI * 2;

        const minSep = (need[a] + need[b]) / 2;
        if (da < minSep) {
          const push = (minSep - da) / 2;
          angles[a] -= push;
          angles[b] += push;
        }
      }
    }

    // normalize back into 0..2pi
    for (let i = 0; i < angles.length; i++) {
      angles[i] = ((angles[i] % (Math.PI * 2)) + Math.PI * 2) % (Math.PI * 2);
    }

    return angles;
  };

  for (let level = 0; level <= maxLevel; level++) {
    const nodes = ((byLevel.get(level) ?? []) as DefNode[])
      .slice()
      .sort((a: DefNode, b: DefNode) => a.id.localeCompare(b.id));

    const count = nodes.length;
    if (!count) continue;

    const r = base + level * ringGap;

    // Spread by angle; avoid a shared horizontal line when count is small.
    const baseOffset = levelOffset(level);

    let baseAngles: number[];
    if (count === 2) {
      // put them on a diagonal rather than left/right
      baseAngles = [baseOffset + Math.PI / 4, baseOffset + (Math.PI + Math.PI / 4)];
    } else if (count === 3) {
      baseAngles = [0, 1, 2].map((i) => baseOffset + (i / 3) * Math.PI * 2 + Math.PI / 6);
    } else {
      baseAngles = nodes.map((_n, i) => baseOffset + (i / count) * Math.PI * 2);
    }

    const angles = relaxAngles(nodes, r, baseAngles);

    for (let i = 0; i < count; i++) {
      const n = nodes[i];
      const a = angles[i];
      placed.set(n.id, { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) });
    }
  }

  return {
    cx,
    cy,
    ringGap,
    base,
    maxLevel,
    pos: placed,
  };
}

function computeLevels(nodes: DefNode[]) {
  const byId = new Map(nodes.map((n) => [n.id, n] as const));
  const visiting = new Set<string>();
  const visited = new Set<string>();

  const dfs = (id: string): number => {
    const n = byId.get(id);
    if (!n) return 0;
    if (visited.has(id)) return n.level ?? 0;
    if (visiting.has(id)) return 0;

    visiting.add(id);
    let level = 0;
    for (const depId of n.deps ?? []) {
      if (!byId.has(depId)) continue;
      level = Math.max(level, 1 + dfs(depId));
    }
    visiting.delete(id);
    visited.add(id);
    n.level = level;
    return level;
  };

  for (const n of nodes) dfs(n.id);
}

function draw(graph: DefGraph) {
  // Ensure dynamic levels exist for rendering.
  computeLevels(graph.nodes);

  setStats(graph);

  const layout = radialLayout(graph);
  lastLayout = layout;

  // nodes that should be "visible" (not learned/ready, but have >=1 incoming on-edge)
  const visibleNodeIds = new Set<string>();
  {
    const byId = new Map(graph.nodes.map((n) => [n.id, n] as const));
    for (const e of graph.edges as Array<{ source: string; target: string }>) {
      // Edge is "on" when the prerequisite (target) is learned.
      const prereq = byId.get(e.target);
      if (!prereq) continue;
      if (learnStateForNode(prereq) !== 'learned') continue;

      // Mark the dependent node as "visible" if it isn't ready/learned.
      const dep = byId.get(e.source);
      if (!dep) continue;
      const base = learnStateForNode(dep);
      if (base === 'off') visibleNodeIds.add(dep.id);
    }
  }

  // rings
  const ringData = d3.range(0, layout.maxLevel + 1).map((level: number) => ({
    level,
    r: layout.base + level * layout.ringGap,
  }));

  gRings
    .selectAll<SVGCircleElement, { level: number; r: number }>('circle.ring')
    .data(ringData, (d) => String(d.level))
    .join((enter) => enter.append('circle').attr('class', 'ring'))
    .attr('cx', layout.cx)
    .attr('cy', layout.cy)
    .attr('r', (d) => d.r);

  // keep hovered ring if any, otherwise keep selected ring
  applyRingHighlight();

  type Edge = { source: string; target: string };

  // Curved edge path generator (quadratic curve via mid-point pulled toward center)
  const edgePath = (d: Edge) => {
    const s = layout.pos.get(d.source);
    const t = layout.pos.get(d.target);
    if (!s || !t) return '';

    const mx = (s.x + t.x) / 2;
    const my = (s.y + t.y) / 2;

    // Pull the control point toward the center so edges arc inward.
    const k = 0.55;
    const cx = mx + (layout.cx - mx) * k;
    const cy = my + (layout.cy - my) * k;

    return `M${s.x},${s.y} Q${cx},${cy} ${t.x},${t.y}`;
  };

  const byId = new Map(graph.nodes.map((n) => [n.id, n] as const));

  const linkSel = gLinks
    .selectAll<SVGPathElement, Edge>('path.link')
    .data(graph.edges as Edge[], (d) => `${d.source}->${d.target}`)
    .join((enter) =>
      enter
        .append('path')
        .attr('class', 'link')
        .attr('fill', 'none')
        .attr('stroke-linecap', 'round')
        .attr('stroke-linejoin', 'round'),
    );

  linkSel
    .attr('d', edgePath)
    // edge styling based on prerequisite learn-state (target)
    .classed('link-on', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      return s === 'learned';
    })
    .classed('link-off', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      return s !== 'learned';
    })
    .attr('stroke', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      // prerequisite not learned => subtle but visible; learned => emphasized
      return s === 'learned' ? 'rgba(226, 232, 240, 0.85)' : 'rgba(148, 163, 184, 0.16)';
    })
    .attr('stroke-width', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      return s === 'learned' ? 2.2 : 1.0;
    })
    .attr('stroke-dasharray', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      return s === 'learned' ? null : '3 5';
    })
    .attr('opacity', 1);

  const nodeSel = gNodes
    .selectAll<SVGGElement, DefNode>('g.node')
    .data(graph.nodes, (d) => d.id)
    .join((enter) => {
      const g = enter.append('g').attr('class', 'node');

      // Bigger base size
      const circleR = 8;
      const leafR = 11;

      // Circle for non-leaves
      g.append('circle').attr('class', 'node-circle').attr('r', circleR);

      // Star for leaves
      const star = d3
        .symbol()
        .type(d3.symbolStar)
        .size(Math.PI * leafR * leafR);
      g.append('path').attr('class', 'node-star').attr('d', star() ?? '');

      // underline/accent ring for leaves
      g.append('circle').attr('class', 'leaf-underline').attr('r', leafR + 4);

      g.append('text').attr('dx', 12).attr('dy', 5);

      // Native SVG tooltip
      g.append('title');

      return g;
    });

  // Update tooltip content for all nodes (enter+update)
  nodeSel
    .select('title')
    .text((d: DefNode) => {
      const kind = d.kind ?? 'leaf';

      const isDefinition = kind === 'leaf';
      const isCategoryish = kind === 'field' || kind === 'category' || kind === 'final-category';

      const path = d.relPath
        ? isDefinition
          ? `${d.relPath}.md`
          : isCategoryish
            ? `${d.relPath}/`
            : d.relPath
        : d.id;

      return `${d.title}\n${path}\n(kind: ${kind}, level: ${d.level ?? 0})`;
    });

  // hover effect
  nodeSel
    .on('mouseenter', (ev: MouseEvent, d: DefNode) => {
      d3.select(ev.currentTarget as SVGGElement).classed('hovering', true);
      setRingHighlight(d.level ?? 0);
    })
    .on('mouseleave', (ev: MouseEvent) => {
      d3.select(ev.currentTarget as SVGGElement).classed('hovering', false);
      setRingHighlight(null);

      // Restore pulsing to the selected node (if any) when not hovering.
      if (selectedNodeId) {
        const sel = gNodes.selectAll<SVGGElement, DefNode>('g.node').filter((n) => n.id === selectedNodeId);
        sel.classed('hovering', true);
      }
    });

  // Ensure the selected node pulses when not hovering another node.
  if (selectedNodeId) {
    gNodes
      .selectAll<SVGGElement, DefNode>('g.node')
      .classed('hovering', (n) => hoveredLevel === null && n.id === selectedNodeId);
  }

  nodeSel.attr('transform', (d) => {
    const p = layout.pos.get(d.id)!;
    return `translate(${p.x},${p.y})`;
  });

  const fillFor = (d: DefNode) => {
    const base = learnStateForNode(d);
    const s: LearnState = base === 'off' && visibleNodeIds.has(d.id) ? 'visible' : base;
    return colorForLearnState(s);
  };

  const stateFor = (d: DefNode): LearnState => {
    const base = learnStateForNode(d);
    return base === 'off' && visibleNodeIds.has(d.id) ? 'visible' : base;
  };

  // show circle only when not a leaf
  nodeSel
    .select<SVGCircleElement>('circle.node-circle')
    .attr('display', (d) => {
      const showAsStar = d.kind === 'leaf' || d.kind === 'final-category';
      return showAsStar ? 'none' : null;
    })
    .attr('fill', (d) => fillFor(d))
    .attr('opacity', 1);

  // show star for leaves and final categories
  nodeSel
    .select<SVGPathElement>('path.node-star')
    .attr('display', (d) => {
      const showAsStar = d.kind === 'leaf' || d.kind === 'final-category';
      return showAsStar ? null : 'none';
    })
    .attr('fill', (d) => fillFor(d))
    .attr('opacity', 1);

  // underline ring only for leaves
  nodeSel
    .select<SVGCircleElement>('circle.leaf-underline')
    .attr('fill', 'none')
    .attr('stroke', (d) => (d.kind === 'leaf' ? fillFor(d) : 'none'))
    .attr('stroke-width', (d) => (d.kind === 'leaf' ? 2 : 0))
    .attr('opacity', (d) => (d.kind === 'leaf' ? 0.9 : 0));

  // label text
  nodeSel
    .select('text')
    .text((d: DefNode) => d.title)
    .attr('fill', '#e6edf3')
    .attr('opacity', (d: DefNode) => (stateFor(d) === 'off' ? 0.22 : 1))
    .attr('text-decoration', 'none')
    .attr('text-decoration-thickness', null)
    .attr('text-underline-offset', null);

  bindInteractions(nodeSel);

  const search = document.getElementById('search') as HTMLInputElement;
  search.oninput = () => {
    const q = normalizeId(search.value);
    const isMatch = (d: DefNode) => q && normalizeId(d.id).includes(q);

    nodeSel
      .selectAll<SVGCircleElement | SVGPathElement, DefNode>('circle.node-circle, path.node-star')
      .attr('stroke', (d) => (isMatch(d) ? '#ef4444' : 'none'))
      .attr('stroke-width', (d) => (isMatch(d) ? 2.5 : 0));
  };
}

// -------------------------------
// Interactive projection model
// -------------------------------

type GroupId = string;

type Raw = {
  def: DefGraph;
  byId: Map<string, DefNode>;
  childrenByPrefix: Map<string, string[]>; // prefix -> ids under that prefix
  fields: string[]; // top-level fields (e.g. mathematics, computer_science)
};

type VisualizationMode = 'definitions' | 'categories';

type UIState = {
  expanded: Set<GroupId>; // group ids that are expanded
  selectedLeaf?: string; // leaf id
  mode: VisualizationMode;
};

const viewerEl = document.getElementById('viewer') as HTMLDivElement;
const viewerTitleEl = document.getElementById('viewerTitle') as HTMLHeadingElement;
const viewerPathEl = document.getElementById('viewerPath') as HTMLDivElement;
const viewerBodyEl = document.getElementById('viewerBody') as HTMLDivElement;
const markLearnedBtn = document.getElementById('markLearned') as HTMLButtonElement | null;

function updateMarkLearnedButton(node?: DefNode) {
  if (!markLearnedBtn) return;
  if (!node || state.mode !== 'definitions' || node.kind !== 'leaf') {
    markLearnedBtn.style.display = 'none';
    markLearnedBtn.disabled = true;
    markLearnedBtn.onclick = null;
    return;
  }

  const s = learnStateForNode(node);
  markLearnedBtn.style.display = '';
  markLearnedBtn.disabled = s !== 'ready';

  markLearnedBtn.onclick = () => {
    // Only works for ready nodes.
    if (learnStateForNode(node) !== 'ready') return;

    learned.add(node.id);
    saveLearnedToStorage();

    // Re-render to update node+edge styles and any newly-ready nodes.
    rerender(true);

    // Behave like clicking "Definitions": clear selection/viewer and refocus to highest active ring
    // so newly-unlocked nodes are brought into view.
    state.selectedLeaf = undefined;
    selectedNodeId = null;
    hideViewer();

    requestAnimationFrame(() => {
      focusHighestActiveRing();
    });
  };
}

function escapeHtml(s: string) {
  return s
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function normalizeMdForViewer(md: string) {
  // 1) drop the first markdown title line (e.g. "# name")
  // 2) normalize CRLF -> LF
  // 3) collapse excessive blank lines
  const lines = md.replace(/\r\n?/g, '\n').split('\n');
  const out: string[] = [];

  let i = 0;
  // drop initial empty lines
  while (i < lines.length && !lines[i].trim()) i++;
  // drop first H1/H2 line
  if (i < lines.length && /^#{1,2}\s+/.test(lines[i].trim())) i++;

  for (; i < lines.length; i++) out.push(lines[i]);

  // trim leading/trailing blank lines
  while (out.length && !out[0].trim()) out.shift();
  while (out.length && !out[out.length - 1].trim()) out.pop();

  // collapse 3+ blank lines to 2
  const collapsed: string[] = [];
  let blank = 0;
  for (const l of out) {
    if (!l.trim()) {
      blank++;
      if (blank <= 2) collapsed.push('');
      continue;
    }
    blank = 0;
    collapsed.push(l);
  }

  return collapsed.join('\n');
}

function selectLeafById(id: string) {
  if (!lastProjected) return;
  const node = lastProjected.nodes.find((n) => n.id === id);
  if (!node) return;

  // Track selection for ring focus + pulsing.
  state.selectedLeaf = id;
  selectedNodeId = id;

  // Re-render (keeps transform) so node/link styles update.
  rerender(true);

  // Focus and pulse on the selected node.
  requestAnimationFrame(() => {
    focusRingOfNode(id);
  });

  // Open viewer content.
  void openLeaf(node);
}

// Keep old helper for internal callers (compat)
function behaviorLikeGraphClick(id: string) {
  selectLeafById(id);
}

function buildDepLinkMap(deps: string[]) {
  const map = new Map<string, { id: string; title: string }>();

  // Prefer the currently projected graph for titles (matches what's on screen)
  const byId = new Map((lastProjected?.nodes ?? []).map((n) => [n.id, n] as const));

  for (const id of deps) {
    const t = byId.get(id)?.title ?? id.split('/').at(-1) ?? id;
    map.set(id, { id, title: t });
  }

  return map;
}

function renderViewerBody(md: string, deps: string[]) {
  const clean = normalizeMdForViewer(md);
  const depMap = buildDepLinkMap(deps);

  // (A) convert markdown links [label](href) into dependency spans (when href points to a known dep)
  // We support both absolute-like "field/path" and simple "field/name" hrefs (no .md).
  const linkRe = /\[([^\]]+)\]\(([^)]+)\)/g;

  const replaced = clean.replace(linkRe, (_m, labelRaw, hrefRaw) => {
    const label = String(labelRaw ?? '').trim();
    const href = String(hrefRaw ?? '').trim().replace(/\.md$/i, '');

    // Try to resolve by exact dep id first.
    let depId: string | undefined;
    if (depMap.has(href)) depId = href;

    // Try to resolve by suffix match: "field/name" against deps containing that suffix.
    if (!depId && href.includes('/')) {
      const suffix = '/' + href.split('/').filter(Boolean).pop();
      const field = href.split('/')[0];
      const candidates = Array.from(depMap.keys()).filter((id) => id.startsWith(field + '/') && id.endsWith(suffix));
      if (candidates.length === 1) depId = candidates[0];
    }

    if (!depId) {
      // Not a known dependency; keep label text only (drop the "(href)" part).
      return escapeHtml(label || href);
    }

    const dep = depMap.get(depId)!;
    // Display only the definition name (title), not "[name](category)".
    return `<span class="dep" data-dep="${escapeHtml(dep.id)}">${escapeHtml(dep.title)}</span>`;
  });

  // (B) Create paragraphs by splitting on blank lines. Within a paragraph, join lines with spaces
  // so there are no visible newline characters.
  const paragraphs = replaced
    .split(/\n\s*\n+/g)
    .map((p) => p.replace(/\s*\n\s*/g, ' ').trim())
    .filter(Boolean);

  viewerBodyEl.innerHTML = paragraphs.map((p) => `<p>${p}</p>`).join('');

  // Bind click handlers for dependency links
  viewerBodyEl.querySelectorAll<HTMLElement>('span.dep[data-dep]').forEach((el) => {
    el.onclick = (ev) => {
      ev.preventDefault();
      ev.stopPropagation();
      const id = el.dataset.dep;
      if (!id) return;
      behaviorLikeGraphClick(id);
    };
  });
}

function showViewer(node: DefNode, md: string) {
  viewerEl.style.display = 'block';
  viewerTitleEl.textContent = node.title;
  viewerPathEl.textContent = `${node.relPath}.md`;
  renderViewerBody(md, node.deps ?? []);
  updateMarkLearnedButton(node);
}

function hideViewer() {
  viewerEl.style.display = 'none';
  viewerTitleEl.textContent = '';
  viewerPathEl.textContent = '';
  viewerBodyEl.textContent = '';
  updateMarkLearnedButton(undefined);
}

function splitPath(id: string) {
  return id.split('/').filter(Boolean);
}

function groupIdForPath(parts: string[], depth: number) {
  return parts.slice(0, depth).join('/');
}

function isLeaf(ownParts: string[]) {
  // Leaf ids are definition relPaths like field/sub/.../name (>=2 segments).
  // (Field nodes in projected graph are synthetic and do NOT come from raw ids.)
  return ownParts.length >= 2;
}

function ownerGroupForLeaf(id: string) {
  const parts = splitPath(id);
  // owning group is the immediate category containing the leaf: everything but last segment
  return parts.slice(0, Math.max(1, parts.length - 1)).join('/');
}

function buildRaw(def: DefGraph): Raw {
  const byId = new Map(def.nodes.map((n) => [n.id, n] as const));

  const fieldsSet = new Set<string>();
  for (const n of def.nodes) {
    const [field] = splitPath(n.id);
    if (field) fieldsSet.add(field);
  }
  const fields = Array.from(fieldsSet).sort();

  // childrenByPrefix: prefix -> leaf ids directly under that prefix (any depth)
  const childrenByPrefix = new Map<string, string[]>();
  for (const n of def.nodes) {
    const parts = splitPath(n.id);
    for (let d = 1; d <= parts.length - 1; d++) {
      const prefix = groupIdForPath(parts, d);
      const arr = childrenByPrefix.get(prefix) ?? [];
      arr.push(n.id);
      childrenByPrefix.set(prefix, arr);
    }
  }

  // de-dupe and sort
  for (const [k, arr] of childrenByPrefix) {
    childrenByPrefix.set(k, Array.from(new Set(arr)).sort());
  }

  return { def, byId, childrenByPrefix, fields };
}

function topLevelGroups(raw: Raw) {
  // Start with just the field nodes.
  return raw.fields.map((f) => ({ id: `field:${f}`, title: f, field: f }));
}

function projectedIdForGroup(groupId: string) {
  // groupId is like mathematics/fundamental ; field is just mathematics
  const parts = splitPath(groupId);
  if (parts.length === 1) return `field:${parts[0]}`;
  return `cat:${groupId}`;
}

function groupIdFromProjected(nodeId: string): string | undefined {
  if (nodeId.startsWith('field:')) return nodeId.slice('field:'.length);
  if (nodeId.startsWith('cat:')) return nodeId.slice('cat:'.length);
  return undefined;
}

function titleForGroup(raw: Raw, groupId: string) {
  const parts = splitPath(groupId);
  return parts[parts.length - 1] ?? groupId;
}

function listDirectChildGroups(raw: Raw, groupId: string) {
  // Return immediate child categories under groupId.
  // BUT: if a child name is also a direct leaf under this group, prefer the leaf (no separate category node).
  const prefix = groupId + '/';

  // Collect direct leaf names for this group.
  const directLeaves = new Set<string>();
  for (const leafId of listDirectLeafChildren(raw, groupId)) {
    const parts = splitPath(leafId);
    directLeaves.add(parts[parts.length - 1] ?? leafId);
  }

  const children = new Set<string>();

  // A child category exists if there is any definition under (groupId + '/child/...')
  for (const id of raw.byId.keys()) {
    if (!id.startsWith(prefix)) continue;
    const rest = id.slice(prefix.length);
    const segs = rest.split('/').filter(Boolean);

    // needs to be deeper than direct leaf: groupId/<child>/<...>
    if (segs.length < 2) continue;

    const child = segs[0];
    if (!child) continue;

    // If there is a direct leaf with the same name, suppress the category node.
    if (directLeaves.has(child)) continue;

    children.add(`${groupId}/${child}`);
  }

  return Array.from(children).sort();
}

function listDirectLeafChildren(raw: Raw, groupId: string) {
  // Direct leaves: defs whose owning group equals groupId
  const prefix = groupId + '/';
  const leaves: string[] = [];
  for (const id of raw.byId.keys()) {
    if (!id.startsWith(prefix)) continue;
    if (ownerGroupForLeaf(id) === groupId) leaves.push(id);
  }
  return leaves.sort();
}

function projectGraph(raw: Raw, state: UIState): DefGraph {
  // Mode behavior:
  // - definitions: show *all* leaves (no categories), no expand/collapse needed
  // - categories: show fields/categories only, expansion allowed, never show leaves

  if (state.mode === 'definitions') {
    const nodes = raw.def.nodes.map((n) => ({
      ...n,
      kind: 'leaf' as NodeKind,
      owningGroup: ownerGroupForLeaf(n.id),
      level: 0,
    }));

    // Edges are already leaf->leaf in raw.def
    const edges = raw.def.edges.map((e) => ({ ...e }));

    // Assign deps from edges
    const depsByNode = new Map<string, string[]>();
    for (const e of edges) {
      const arr = depsByNode.get(e.source) ?? [];
      arr.push(e.target);
      depsByNode.set(e.source, arr);
    }
    for (const n of nodes) {
      n.deps = depsByNode.get(n.id) ?? (n.deps ?? []);
      n.level = 0;
    }

    computeLevels(nodes);
    return { nodes, edges };
  }

  // categories mode
  const nodes: DefNode[] = [];
  const addNode = (n: DefNode) => nodes.push(n);

  const isGroupExpanded = (gid: string) => state.expanded.has(gid);

  // Helper: find the set of leaf ids represented by a visible group node.
  // If the group is expanded, it should represent the remainder of its subtree that is NOT covered by any visible descendant group nodes.
  // If it's not expanded, it represents its full subtree.
  const representedLeavesForGroup = (gid: string, byId: Map<string, DefNode>) => {
    const all = new Set(raw.childrenByPrefix.get(gid) ?? []);

    // subtract leaves that are owned by any visible descendant group
    const descendants = Array.from(byId.keys())
      .map((nid) => groupIdFromProjected(nid))
      .filter((x): x is string => !!x)
      .filter((dgid) => dgid !== gid && dgid.startsWith(gid + '/'))
      // prefer deepest first so we subtract larger chunks early
      .sort((a, b) => b.length - a.length);

    for (const dgid of descendants) {
      const sub = raw.childrenByPrefix.get(dgid) ?? [];
      for (const leafId of sub) all.delete(leafId);
    }

    return Array.from(all);
  };

  for (const f of raw.fields) {
    if (!isGroupExpanded(f)) {
      addNode({
        id: projectedIdForGroup(f),
        title: f,
        relPath: f,
        filePath: '',
        deps: [],
        level: 0,
        kind: 'field',
        owningGroup: undefined,
      });
      continue;
    }

    // expanded field: show subcategories only (NO leaves)
    for (const childG of listDirectChildGroups(raw, f)) {
      const hasChildren = listDirectChildGroups(raw, childG).length > 0;
      addNode({
        id: projectedIdForGroup(childG),
        title: titleForGroup(raw, childG),
        relPath: childG,
        filePath: '',
        deps: [],
        level: 0,
        kind: hasChildren ? 'category' : 'final-category',
        owningGroup: f,
      });
    }
  }

  // Expand visible categories when in expanded state (category disappears)
  let changed = true;
  while (changed) {
    changed = false;

    const visibleCats = nodes.filter((n) => n.kind === 'category');
    for (const cat of visibleCats) {
      const gid = groupIdFromProjected(cat.id);
      if (!gid) continue;
      if (!isGroupExpanded(gid)) continue;

      const idx = nodes.findIndex((n) => n.id === cat.id);
      if (idx >= 0) nodes.splice(idx, 1);

      for (const childG of listDirectChildGroups(raw, gid)) {
        const hasChildren = listDirectChildGroups(raw, childG).length > 0;
        addNode({
          id: projectedIdForGroup(childG),
          title: titleForGroup(raw, childG),
          relPath: childG,
          filePath: '',
          deps: [],
          level: 0,
          kind: hasChildren ? 'category' : 'final-category',
          owningGroup: gid,
        });
      }

      changed = true;
      break;
    }
  }

  const byId = new Map<string, DefNode>();
  for (const n of nodes) byId.set(n.id, n);

  const visible = Array.from(byId.values());

  const pickRepresentative = (rawId: string): string | undefined => {
    if (!raw.byId.has(rawId)) return undefined;

    // Leaves are not visible in categories mode. Find the nearest visible group.
    const parts = splitPath(rawId);
    for (let d = parts.length - 1; d >= 1; d--) {
      const gid = groupIdForPath(parts, d);
      const cand = projectedIdForGroup(gid);
      if (byId.has(cand)) return cand;
      if (d === 1) {
        const f = parts[0];
        const fieldNode = projectedIdForGroup(f);
        if (byId.has(fieldNode)) return fieldNode;
      }
    }

    return undefined;
  };

  const edgeKey = new Set<string>();
  const edges: Array<{ source: string; target: string }> = [];

  for (const n of visible) {
    const gid = groupIdFromProjected(n.id);
    if (!gid) continue;

    const leafIds = representedLeavesForGroup(gid, byId);

    const deps = new Set<string>();
    for (const leafId of leafIds) {
      const leaf = raw.byId.get(leafId);
      if (!leaf) continue;
      for (const d of leaf.deps) deps.add(d);
    }

    for (const depRawId of deps) {
      const rep = pickRepresentative(depRawId);
      if (!rep) continue;
      if (rep === n.id) continue;
      const k = `${n.id}->${rep}`;
      if (edgeKey.has(k)) continue;
      edgeKey.add(k);
      edges.push({ source: n.id, target: rep });
    }
  }

  // assign deps on projected nodes from edges
  const depsByNode = new Map<string, string[]>();
  for (const e of edges) {
    const arr = depsByNode.get(e.source) ?? [];
    arr.push(e.target);
    depsByNode.set(e.source, arr);
  }
  for (const n of visible) {
    n.deps = depsByNode.get(n.id) ?? [];
    n.level = 0;
  }

  computeLevels(visible);
  return { nodes: visible, edges };
}

function bindInteractions(nodeSel: d3.Selection<SVGGElement, DefNode, SVGGElement, unknown>) {
  // Ensure we don't overwrite existing hover handlers added in draw()
  nodeSel
    .on('click.interact', (ev: MouseEvent, d: DefNode) => {
      ev.preventDefault();
      ev.stopPropagation();

      // Definitions mode: single left-click does the full experience.
      if (state.mode === 'definitions') {
        selectLeafById(d.id);
        return;
      }

      // Categories mode: do not expand final categories.
      if (d.kind === 'final-category') return;

      const gid = groupIdFromProjected(d.id);
      if (!gid) return;

      if (state.expanded.has(gid)) state.expanded.delete(gid);
      else state.expanded.add(gid);

      hideViewer();
      rerender(true);
    })
    .on('contextmenu.interact', (ev: MouseEvent, d: DefNode) => {
      ev.preventDefault();
      ev.stopPropagation();

      // Definitions mode: no special right-click behavior.
      if (state.mode === 'definitions') return;

      const gid = d.owningGroup ?? groupIdFromProjected(d.id);
      if (!gid) return;

      for (const eg of Array.from(state.expanded) as string[]) {
        if (eg === gid || eg.startsWith(gid + '/')) state.expanded.delete(eg);
      }

      hideViewer();
      rerender(true);
    });
}

// -------------------------------
// App bootstrap / state
// -------------------------------

const rawPromise: Promise<Raw> = fetch('./defs.json')
  .then((r) => r.json())
  .then((def: DefGraph) => buildRaw(def));

const state: UIState = {
  expanded: new Set<GroupId>(),
  selectedLeaf: undefined,
  mode: 'definitions',
};

let lastProjected: DefGraph | null = null;

function focusHighestActiveRing() {
  if (!lastProjected) return;

  const maxLevel = Math.max(0, ...lastProjected.nodes.map((n) => n.level ?? 0));

  // Prefer highest ring that has something actionable/achieved.
  let best = maxLevel;
  for (let level = maxLevel; level >= 0; level--) {
    const has = lastProjected.nodes.some((n) => {
      if ((n.level ?? 0) !== level) return false;
      const s = learnStateForNode(n);
      return s === 'ready' || s === 'learned';
    });
    if (has) {
      best = level;
      break;
    }
  }

  focusRing(best);
  setRingHighlight(best);
}

function rerender(keepTransform: boolean) {
  const current = keepTransform ? d3.zoomTransform(svg.node() as any) : null;

  rawPromise
    .then((raw) => {
      const projected = projectGraph(raw, state);
      lastProjected = projected;
      draw(projected);

      // Keep current zoom/pan transform when re-rendering due to UI actions.
      if (current) {
        svg.call(zoom.transform as any, current);
      }

      // Keep ring highlight consistent with selection after redraw.
      applyRingHighlight();

      // If nothing is selected, focus + underline the highest active ring.
      // Do it in the next frame so layout+DOM are settled (same timing as button behavior).
      if (state.mode === 'definitions' && !state.selectedLeaf) {
        requestAnimationFrame(() => {
          focusHighestActiveRing();
        });
      }

      // Keep viewer updated if we have a selected leaf.
      if (state.mode === 'definitions' && state.selectedLeaf) {
        const n = projected.nodes.find((x: DefNode) => x.id === state.selectedLeaf);
        if (n) void openLeaf(n);
      }
    })
    .catch((err) => {
      // eslint-disable-next-line no-console
      console.error(err);
    });
}

function focusRing(level: number) {
  if (!lastProjected) return;

  // Use the actual layout used during the last draw() to avoid ring spacing mismatch.
  const layout = lastLayout ?? radialLayout(lastProjected);
  const r = layout.base + level * layout.ringGap;

  // Fit the circle to viewport.
  const pad = 60;
  const width = W();
  const height = H();

  const diameter = 2 * r + pad;
  const scale = Math.max(0.12, Math.min(6, Math.min(width / diameter, height / diameter)));

  const tx = width / 2 - layout.cx * scale;
  const ty = height / 2 - layout.cy * scale;

  svg
    .transition()
    .duration(650)
    .call(zoom.transform as any, d3.zoomIdentity.translate(tx, ty).scale(scale));
}

function focusRingOfNode(id: string) {
  if (!lastProjected) return;
  const n = lastProjected.nodes.find((x: DefNode) => x.id === id);
  if (!n) return;
  focusRing(n.level ?? 0);
}

async function openLeaf(node: DefNode) {
  if (!node.relPath) return;

  // Ensure pulsing matches whatever opened the viewer.
  selectedNodeId = node.id;
  applyRingHighlight();

  // Use preloaded content from defs.json if available
  const md = node.content || '(no content)';
  showViewer(node, md);
}

// Initial render
rerender(false);

// UI wiring
const overviewBtn = (document.getElementById('focus') ?? document.getElementById('overview')) as HTMLButtonElement | null;
overviewBtn?.addEventListener('click', () => {
  if (!lastProjected) return;
  // Fit whole graph: focus max ring.
  const maxLevel = Math.max(0, ...lastProjected.nodes.map((n) => n.level ?? 0));
  focusRing(maxLevel);
  setRingHighlight(maxLevel);
});

const resetBtn =
  (document.getElementById('resetProgress') ?? document.getElementById('reset')) as HTMLButtonElement | null;
resetBtn?.addEventListener('click', () => {
  clearLearnedProgress();
  saveLearnedToStorage();
  hideViewer();
  rerender(true);
});

const modeDefinitionsBtn = document.getElementById('modeDefinitions') as HTMLButtonElement | null;
modeDefinitionsBtn?.addEventListener('click', () => {
  state.mode = 'definitions';

  // Reset selection + viewer when switching back to Definitions.
  state.selectedLeaf = undefined;
  selectedNodeId = null;
  hideViewer();

  // Re-render, then focus to the highest active ring (same logic as init).
  rerender(true);

  requestAnimationFrame(() => {
    focusHighestActiveRing();
  });
});

const modeCategoriesBtn = document.getElementById('modeCategories') as HTMLButtonElement | null;
modeCategoriesBtn?.addEventListener('click', () => {
  // Categories mode intentionally disabled/experimental.
  return;
});
