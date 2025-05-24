from enum import StrEnum

from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class Track(StrEnum):
    DATA_STRUCTURES = "data_structures"


# TODO(K4liber): create a mapping DefinitionKey -> Track

_track_to_definitions: dict[Track, list[DefinitionKey]] = {
    Track.DATA_STRUCTURES: [
        DefinitionKey(name="set", field=Field.MATHEMATICS),
        DefinitionKey(name="multiset", field=Field.MATHEMATICS),
        DefinitionKey(name="finite_set", field=Field.MATHEMATICS),
        DefinitionKey(name="function", field=Field.MATHEMATICS),
        DefinitionKey(name="relation", field=Field.MATHEMATICS),
        DefinitionKey(name="object", field=Field.MATHEMATICS),
        DefinitionKey(name="graph", field=Field.MATHEMATICS),
        DefinitionKey(name="node", field=Field.MATHEMATICS),
        DefinitionKey(name="edge", field=Field.MATHEMATICS),
        DefinitionKey(name="path", field=Field.MATHEMATICS),
        DefinitionKey(name="cycle", field=Field.MATHEMATICS),
        DefinitionKey(name="graph_distance", field=Field.MATHEMATICS),
        DefinitionKey(name="adjacency_list", field=Field.MATHEMATICS),
        DefinitionKey(name="bipartite_graph", field=Field.MATHEMATICS),
        DefinitionKey(name="directed_graph", field=Field.MATHEMATICS),
        DefinitionKey(name="directed_acyclic_graph", field=Field.MATHEMATICS),
        DefinitionKey(name="tree", field=Field.MATHEMATICS),
        DefinitionKey(name="leaf", field=Field.MATHEMATICS),
        DefinitionKey(name="subtree", field=Field.MATHEMATICS),
        DefinitionKey(name="minimum_spanning_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="k_ary_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="binary_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="balanced_binary_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="unbalanced_binary_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="complete_binary_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="b_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="binary_search_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="interval_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="avl_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="red_black_tree", field=Field.MATHEMATICS),
        DefinitionKey(name="information", field=Field.MATHEMATICS),
        DefinitionKey(name="data", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="bit", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="data_structure", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="bit_field", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="object", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="data_type", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="operation", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="abstract_data_type", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="primitive_data_type", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="map", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="boolean", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="collection", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="list", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="queue", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="stack", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="priority_queue", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="bag", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="set", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="heap_tree", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="array", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="linked_list", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="associative_array", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="hash_table", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="character_encoding", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="utf", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="utf_8", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="string", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="unicode", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="ascii", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="extended_ascii", field=Field.COMPUTER_SCIENCE),
        DefinitionKey(name="trie", field=Field.COMPUTER_SCIENCE),
    ]
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
    track = Track.DATA_STRUCTURES
    _dump_track_md(track=track, out_path=f"{track}.md")
