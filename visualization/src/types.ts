export type NodeKind = 'field' | 'category' | 'final-category' | 'leaf';

export type DefNode = {
  /**
   * Unique id used throughout the visualization.
   * In the current generator this equals relPath (slashes preserved).
   */
  id: string;

  title: string;

  /** path from index.md (without .md) */
  relPath: string;

  /** client-only usage; kept for compatibility with generator output */
  filePath: string;

  /** dependency ids (ids resolve to relPaths) */
  deps: string[];

  /**
   * Dynamic layout level (computed in the UI on the current projected graph).
   * Not persisted in defs.json.
   */
  level?: number;

  /** interactive projection metadata */
  kind?: NodeKind;

  /** If present, right-click collapses this whole group id. */
  owningGroup?: string;

  /** Preloaded markdown content for viewer */
  content?: string;
};

export type DefGraph = {
  nodes: DefNode[];
  edges: Array<{ source: string; target: string }>; // source -> target (source depends on target)
};
