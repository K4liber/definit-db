from enum import StrEnum

from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class Track(StrEnum):
    DATA_STRUCTURES = "data_structures"
    ALGORITHMS = "algorithms"


_definition_key_to_track: dict[DefinitionKey, Track] = {
    # Mathematics field index
    DefinitionKey(name="object", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="information", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="sequence", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="finite_sequence", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="instruction", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="operation", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="relation", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="set", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="finite_set", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="function", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="hash_function", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="multiset", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="label", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="problem", field=Field.MATHEMATICS): Track.ALGORITHMS,
    DefinitionKey(name="criterion", field=Field.MATHEMATICS): Track.ALGORITHMS,
    DefinitionKey(name="optimal_solution", field=Field.MATHEMATICS): Track.ALGORITHMS,
    DefinitionKey(name="optimal_substructure", field=Field.MATHEMATICS): Track.ALGORITHMS,
    DefinitionKey(name="solution", field=Field.MATHEMATICS): Track.ALGORITHMS,
    DefinitionKey(name="subproblem", field=Field.MATHEMATICS): Track.ALGORITHMS,
    DefinitionKey(name="algorithm", field=Field.MATHEMATICS): Track.ALGORITHMS,
    DefinitionKey(name="graph", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="node", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="edge", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="adjacency_list", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="bipartite_graph", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="cycle", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="directed_acyclic_graph", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="directed_graph", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="graph_distance", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="path", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="avl_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="b_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="balanced_binary_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="binary_search_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="binary_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="complete_binary_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="interval_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="k_ary_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="leaf", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="minimum_spanning_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="red_black_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="subtree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    DefinitionKey(name="unbalanced_binary_tree", field=Field.MATHEMATICS): Track.DATA_STRUCTURES,
    # Computer science field index
    DefinitionKey(name="object", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="data", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="data_structure", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="data_type", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="operation", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="bit", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="abstract_data_type", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="bit_field", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="collection", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="map", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="primitive_data_type", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="associative_array", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="hash_table", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="bag", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="set", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="heap_tree", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="array", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="linked_list", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="list", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="priority_queue", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="queue", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="stack", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="boolean", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="integer", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="character_encoding", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="ascii", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="extended_ascii", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="utf", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="utf_8", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="unicode", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="string", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="substring", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="trie", field=Field.COMPUTER_SCIENCE): Track.DATA_STRUCTURES,
    DefinitionKey(name="graph_labeling", field=Field.COMPUTER_SCIENCE): Track.ALGORITHMS,
    DefinitionKey(name="graph_coloring", field=Field.COMPUTER_SCIENCE): Track.ALGORITHMS,
    DefinitionKey(name="vertex_coloring", field=Field.COMPUTER_SCIENCE): Track.ALGORITHMS,
    DefinitionKey(name="overlapping_subproblems", field=Field.COMPUTER_SCIENCE): Track.ALGORITHMS,
    DefinitionKey(name="hash_collision", field=Field.COMPUTER_SCIENCE): Track.ALGORITHMS,
    DefinitionKey(name="rolling_hash", field=Field.COMPUTER_SCIENCE): Track.ALGORITHMS,
    DefinitionKey(name="rabin_karp_algorithm", field=Field.COMPUTER_SCIENCE): Track.ALGORITHMS,
}

_track_to_definitions: dict[Track, list[DefinitionKey]] = {
    track: [
        definition_key
        for definition_key, definition_track in _definition_key_to_track.items()
        if definition_track == track
    ]
    for track in Track
}


def get_track_list(track: Track) -> list[DefinitionKey]:
    return _track_to_definitions[track]


def _dump_track_md(track: Track, out_path: str):
    """Dump the track as an .md file in the same form as index.md (see attachments)."""
    lines: list[str] = []

    for key in get_track_list(track):
        # Compose relative path: <field>/<name>
        lines.append(f"- [{key.name}]({key.field.lower()}/{key.name})")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    for track in Track:
        _dump_track_md(track=track, out_path=f"{track}.md")
