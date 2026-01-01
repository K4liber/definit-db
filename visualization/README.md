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

## Interactive behavior (current)

### Panel layout

- **Top (centered)**: mode buttons (Definitions / Categories)
- **Bottom (centered)**: option buttons (Overview / Reset progress)

### Modes

At the moment, the app runs in **Definitions** mode only.

- **Definitions**: shows *all* definition nodes (leaves) at once.
- **Categories**: **experimental and temporarily disabled** (see section below).

Re-clicking **Definitions** also resets the visualization back to the initial view.

### Buttons

- **Overview**: fits the whole graph into view (zoom-to-fit).
- **Reset progress**: clears all learned nodes (removes saved progress from browser storage) and resets the view.

### Initial view / starting focus

On startup (and whenever you click **Definitions**), the app focuses the view on the **highest ring/level** that contains at least one node that is:

- **ready-to-learn**, or
- **already-learned**

If no such nodes exist, it falls back to **Overview**.

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

When a definition is open in the side viewer, you will see a **“Mark as learned”** button.

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

## Search

Use the **“Search node by id/title…”** input to quickly highlight matching nodes.

- Matching is performed against the node `id` (which equals the definition `relPath`).
- Matches are indicated by a **red outline** around the node shape.

## Mouse interactions

- **Hover** (any node)
  - Highlights the hovered node’s **ring/level**.

- **Left click** (definition node)
  - Marks the node as **selected**.
  - Focuses/centers the view on the selected node’s **ring/level**.
  - Opens the definition content in the side viewer by loading:
    - `definitions/<relPath>.md` via `/md/<relPath>.md`

### Ring selection + hover priority

- When a node is selected, its ring stays highlighted.
- When hovering another node, the hovered ring is highlighted instead.
- When hover ends, the highlight returns to the selected ring.

### Selected node emphasis

- The selected node pulses together with the currently hovered node

## Categories mode (experimental, temporarily disabled)

There is an experimental **Categories** mode intended to provide an aggregated, expandable view of the same dependency graph.

- The UI still shows a **Categories** button, but it is disabled.
- The code path exists for future iteration/removal and should be treated as unstable.

Intended behavior (when enabled):

- Start with only field nodes.
- Click to expand/collapse subcategories.
- Do **not** show definition leaf nodes.
- Mark a category with no further subcategories as a final category (rendered as a star).

## Mobile adapted view

UI of the visualization is mobile adapted. The graph panel with graph visualized is always a rectangle in order to shown a level ring on a full panel.

At the top of the screen we have the menu panel with the following buttons:
- "Progress", focusing on the most outer ring with at least one definition in a state different than "off"
- "Overview", focusing on the whole definitions graph
- "Reset progress", resetting the current learning progress

At the bottom of the screen we have the functional panel that can be hidden/shown using a button on the left side of the panel. When it is hidden then only a button to show it is visible on the panel. When it is shown it contains:
- "Search", input for the searching functionality
- "Content", content of an active definition
- "Graph details", stats of a graph e.g. number of nodes
The functional panel keeps it state, so even if it is hidden and then showed again, the state will remain and be displayed again.
