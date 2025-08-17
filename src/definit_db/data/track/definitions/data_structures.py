from definit_db.data.field.computer_science.definitions.data_structure.abstract_data_type import ABSTRACT_DATA_TYPE
from definit_db.data.field.computer_science.definitions.data_structure.bit_field import BIT_FIELD
from definit_db.data.field.computer_science.definitions.data_structure.collection.associative_array import (
    ASSOCIATIVE_ARRAY,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.bag import BAG
from definit_db.data.field.computer_science.definitions.data_structure.collection.collection import COLLECTION
from definit_db.data.field.computer_science.definitions.data_structure.collection.hash_table import HASH_TABLE
from definit_db.data.field.computer_science.definitions.data_structure.collection.heap_tree import HEAP_TREE
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.linked_list import LINKED_LIST
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.data_structure.collection.priority_queue import PRIORITY_QUEUE
from definit_db.data.field.computer_science.definitions.data_structure.collection.queue import QUEUE
from definit_db.data.field.computer_science.definitions.data_structure.collection.set import SET as CS_SET
from definit_db.data.field.computer_science.definitions.data_structure.collection.stack import STACK
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.ascii import ASCII
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.extended_ascii import (
    EXTENDED_ASCII,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.substring import SUBSTRING
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.unicode import UNICODE
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.utf import UTF
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.utf_8 import UTF_8
from definit_db.data.field.computer_science.definitions.data_structure.collection.trie import TRIE
from definit_db.data.field.computer_science.definitions.data_structure.map import MAP
from definit_db.data.field.computer_science.definitions.data_structure.primitive.boolean import BOOLEAN
from definit_db.data.field.computer_science.definitions.data_structure.primitive.integer import INTEGER
from definit_db.data.field.computer_science.definitions.data_structure.primitive_data_type import PRIMITIVE_DATA_TYPE
from definit_db.data.field.computer_science.definitions.foundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.computer_science.definitions.foundamental.data_structure import (
    DATA_STRUCTURE as CS_DATA_STRUCTURE,
)
from definit_db.data.field.computer_science.definitions.foundamental.data_type import DATA_TYPE
from definit_db.data.field.computer_science.definitions.foundamental.object import OBJECT as CS_OBJECT
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION as CS_OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.finite_sequence import FINITE_SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.finite_set import FINITE_SET
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.multiset import MULTISET
from definit_db.data.field.mathematics.definitions.fundamental.notations.label import LABEL
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.graph.adjacency_list import ADJACENCY_LIST
from definit_db.data.field.mathematics.definitions.graph.bipartite_graph import BIPARTITE_GRAPH
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.directed_acyclic_graph import DIRECTED_ACYCLIC_GRAPH
from definit_db.data.field.mathematics.definitions.graph.directed_graph import DIRECTED_GRAPH
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.graph.tree.avl_tree import AVL_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.b_tree import B_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.balanced_binary_tree import BALANCED_BINARY_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.binary_search_tree import BINARY_SEARCH_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.binary_tree import BINARY_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.complete_binary_tree import COMPLETE_BINARY_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.interval_tree import INTERVAL_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.k_ary_tree import K_ARY_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.leaf import LEAF
from definit_db.data.field.mathematics.definitions.graph.tree.minimum_spanning_tree import MINIMUM_SPANNING_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.red_black_tree import RED_BLACK_TREE
from definit_db.data.field.mathematics.definitions.graph.tree.subtree import SUBTREE
from definit_db.data.field.mathematics.definitions.graph.tree.tree import TREE
from definit_db.data.field.mathematics.definitions.graph.tree.unbalanced_binary_tree import UNBALANCED_BINARY_TREE
from definit_db.data.track.definitions.track_definitions_abstract import TrackDefinitionsAbstract
from definit_db.definition.definition_key import DefinitionKey

_definition_keys: tuple[DefinitionKey, ...] = (
    OBJECT.key,
    INFORMATION.key,
    SEQUENCE.key,
    FINITE_SEQUENCE.key,
    INSTRUCTION.key,
    OPERATION.key,
    RELATION.key,
    SET.key,
    FINITE_SET.key,
    FUNCTION.key,
    HASH_FUNCTION.key,
    MULTISET.key,
    LABEL.key,
    GRAPH.key,
    NODE.key,
    EDGE.key,
    ADJACENCY_LIST.key,
    BIPARTITE_GRAPH.key,
    CYCLE.key,
    DIRECTED_ACYCLIC_GRAPH.key,
    DIRECTED_GRAPH.key,
    GRAPH_DISTANCE.key,
    PATH.key,
    AVL_TREE.key,
    B_TREE.key,
    BALANCED_BINARY_TREE.key,
    BINARY_SEARCH_TREE.key,
    BINARY_TREE.key,
    COMPLETE_BINARY_TREE.key,
    INTERVAL_TREE.key,
    K_ARY_TREE.key,
    LEAF.key,
    MINIMUM_SPANNING_TREE.key,
    RED_BLACK_TREE.key,
    SUBTREE.key,
    TREE.key,
    UNBALANCED_BINARY_TREE.key,
    CS_OBJECT.key,
    DATA.key,
    CS_DATA_STRUCTURE.key,
    DATA_TYPE.key,
    CS_OPERATION.key,
    BIT.key,
    ABSTRACT_DATA_TYPE.key,
    BIT_FIELD.key,
    COLLECTION.key,
    MAP.key,
    PRIMITIVE_DATA_TYPE.key,
    ASSOCIATIVE_ARRAY.key,
    HASH_TABLE.key,
    BAG.key,
    CS_SET.key,
    HEAP_TREE.key,
    ARRAY.key,
    LINKED_LIST.key,
    LIST.key,
    PRIORITY_QUEUE.key,
    QUEUE.key,
    STACK.key,
    BOOLEAN.key,
    INTEGER.key,
    CHARACTER_ENCODING.key,
    ASCII.key,
    EXTENDED_ASCII.key,
    UTF.key,
    UTF_8.key,
    UNICODE.key,
    STRING.key,
    SUBSTRING.key,
    TRIE.key,
)


class TrackDefinitionsDataStructures(TrackDefinitionsAbstract):
    @staticmethod
    def get_track_definition_keys() -> tuple[DefinitionKey, ...]:
        """Get the track definition keys."""
        return _definition_keys
