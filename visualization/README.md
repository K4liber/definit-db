# DefinIT - Data Structures and Algorithms — Visualization

This folder contains a small TypeScript + Vite + D3 app that visualizes the definitions database as a **directed acyclic graph (DAG)** arranged in **concentric circles** (radial levels).

- **Level 0 (inner ring)**: definitions with **no dependencies**
- **Level N**: definitions that depend (directly or indirectly) on lower levels

The graph data is generated from the following markdown files:
- `src/definit_db/data_md/index.md` (list of all definitions)
- `src/definit_db/data_md/definitions/**.md` (definition content, used to extract dependencies)

## Prerequisites

- Node.js (recommended: Node 18+)
- npm

## Install

From the repo root:

1. Go to the visualization folder:
   - `cd visualization`

2. Install dependencies:
   - `npm install`

## Generate graph data

Generate `public/defs.json` from the markdown database:

- `npm run gen:data`

This reads:
- `../src/definit_db/data_md/index.md`
- `../src/definit_db/data_md/definitions/**/*.md`

and writes:
- `visualization/public/defs.json`

If generation fails with a cycle error, it usually means dependency extraction is too permissive (e.g. self-references or non-definition links were interpreted as dependencies). See **Troubleshooting** below.

## Run the dev server

Start the app:

- `npm run dev`

Open the URL printed by Vite (typically `http://localhost:5173`).

## Build + preview

- `npm run build`
- `npm run preview`


## Troubleshooting

### “Cycle detected …” during `npm run gen:data`

The generator enforces DAG constraints. A cycle error usually comes from one of:

- A real cycle in the underlying definition dependencies
- A **false-positive dependency** (most common), e.g. a definition linking to itself or using a generic markdown link that looks like a dependency.

The generator tries to reduce false positives by:

- Ignoring self-dependencies
- Only keeping dependencies that exist in `index.md`

## Interactive behavior

### Progress + learning

- Nodes are rendered in concentric rings/levels.
- Learning state is persisted in the browser (via `localStorage`).

### Search

Use the “Search node by id/title…” input to highlight matching nodes.

- Matching is performed against the node `id` (which equals the definition `relPath`) and title.
- Matches are indicated by a red outline around the node.

### Selection + focus + viewer

- **Hover** highlights the hovered node’s ring/level.
- **Left click** selects a node and focuses/centers the view on its ring/level.
- Selecting a node loads its markdown and shows it in the bottom panel **Definition** tab.
- If the bottom panel is collapsed, selecting a node will auto-expand it.

### Initial view / starting focus

On startup (and after resetting progress), the app focuses the view on the highest ring/level that contains at least one node that is **ready-to-learn** or **already-learned**. If no such nodes exist, it falls back to **Overview**.

## Learning states

### Node states and colors

Definition nodes (leaves) are colored by learning/progress state:

- **Off**: *barely visible* gray (high transparency)
- **Visible**: gray
- **Ready-to-learn**: yellow
- **Already-learned**: green

### State rules

- A node is **already-learned** once you explicitly mark it as learned.
- A node is **ready-to-learn** when **all of its dependencies are already-learned** (nodes with no dependencies are ready).
- A node is **visible** when it is **not learned**, **not ready**, and has **at least one incoming “on” edge**.
- Otherwise the node is **off**.

Learned state is persisted in the browser (via `localStorage`).

### Off node label fading

For nodes in the **off** state, the **label text is also faded** (lower opacity), so the background graph is present but unobtrusive.

### Mark as learned

When a definition is open, you will see a **“Mark as learned”** button.

- It is enabled only when the current node is **ready-to-learn**.
- Clicking it marks that node as **already-learned** and updates the graph.

### Reset progress

**Reset progress** clears the learned set from memory and browser storage, re-renders the graph, and re-applies the initial focus behavior.

## Edges

### Direction / meaning

Each edge is `source -> target`, meaning:

- **source depends on target**
- `target` is a prerequisite for `source`

### Styling

- Edges are rendered as **curved paths** (they arc inward toward the center).
- Edges are styled based on the **prerequisite node** (`target`) state:
  - **On edge**: prerequisite is **learned** (more visible)
  - **Off edge**: prerequisite is **not learned** (still visible but subtler, typically dashed)

## UI description

The visualization UI is designed to work well on both desktop and mobile.

### Layout overview

The UI is split into three vertical regions:

- **Top menu**: primary view controls (Progress / Overview / Reset progress)
- **Main panel**
  - **Graph canvas** (SVG visualization)
  - **Bottom panel** (details)
    - Expanded: graph and bottom panel share height (50/50 split)
    - Collapsed: graph uses full height
- **Bottom controls**: panel toggle (▲/▼) and the Search input

### Bottom panel contents (tabs)

- **Definition** tab: selected definition content + “Mark as learned” action
- **Graph** tab: graph statistics

### Persistence

The bottom panel collapsed/expanded state is persisted in `localStorage`.

## Expanding/collapsing categories

Each definition has a category 