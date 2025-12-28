from definit.definition.definition import Definition

from definit_db.data.field.computer_science.definitions.algorithms.bit_manipulation import BIT_MANIPULATION
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.graph_coloring import (
    GRAPH_COLORING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.graph_labeling import (
    GRAPH_LABELING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.vertex_coloring import (
    VERTEX_COLORING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.hash_collision import HASH_COLLISION
from definit_db.data.field.computer_science.definitions.algorithms.problems.rolling_hash import ROLLING_HASH
from definit_db.data.field.computer_science.definitions.algorithms.searching.string.rabin_karp_algorithm import (
    RABIN_KARP_ALGORITHM,
)
from definit_db.data.field.computer_science.definitions.data_structure.abstract_data_type import ABSTRACT_DATA_TYPE
from definit_db.data.field.computer_science.definitions.data_structure.bit_field import BIT_FIELD
from definit_db.data.field.computer_science.definitions.data_structure.collection.associative_array import (
    ASSOCIATIVE_ARRAY,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.bag import BAG
from definit_db.data.field.computer_science.definitions.data_structure.collection.collection import COLLECTION
from definit_db.data.field.computer_science.definitions.data_structure.collection.hash_table import HASH_TABLE
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.linked_list import LINKED_LIST
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.data_structure.collection.priority_queue import PRIORITY_QUEUE
from definit_db.data.field.computer_science.definitions.data_structure.collection.queue import QUEUE
from definit_db.data.field.computer_science.definitions.data_structure.collection.set import SET
from definit_db.data.field.computer_science.definitions.data_structure.collection.stack import STACK
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.ascii import ASCII
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.extended_ascii import (
    EXTENDED_ASCII,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.regular_expression import (
    REGULAR_EXPRESSION,
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
from definit_db.data.field.computer_science.definitions.foundamental.arithmetic_right_shift import (
    ARITHMETIC_RIGHT_SHIFT,
)
from definit_db.data.field.computer_science.definitions.foundamental.binary_fractions import BINARY_FRACTIONS
from definit_db.data.field.computer_science.definitions.foundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.foundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.foundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.cache import CACHE
from definit_db.data.field.computer_science.definitions.foundamental.call_stack import CALL_STACK
from definit_db.data.field.computer_science.definitions.foundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.foundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.concurrency import CONCURRENCY
from definit_db.data.field.computer_science.definitions.foundamental.core import CORE
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.computer_science.definitions.foundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.foundamental.data_type import DATA_TYPE
from definit_db.data.field.computer_science.definitions.foundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.foundamental.heap_memory import HEAP_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.heap_overflow import HEAP_OVERFLOW
from definit_db.data.field.computer_science.definitions.foundamental.logical_right_shift import LOGICAL_RIGHT_SHIFT
from definit_db.data.field.computer_science.definitions.foundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.foundamental.object import OBJECT
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.parallelism import PARALLELISM
from definit_db.data.field.computer_science.definitions.foundamental.processor import PROCESSOR
from definit_db.data.field.computer_science.definitions.foundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.foundamental.random_access_memory import RANDOM_ACCESS_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.right_shift import RIGHT_SHIFT
from definit_db.data.field.computer_science.definitions.foundamental.stack_memory import STACK_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.stack_overflow import STACK_OVERFLOW
from definit_db.data.field.computer_science.definitions.foundamental.twos_complement import TWOS_COMPLEMENT
from definit_db.data.field.computer_science.definitions.foundamental.variable import VARIABLE

field_index: list[Definition] = [
    OBJECT,
    DATA,
    DATA_STRUCTURE,
    DATA_TYPE,
    OPERATION,
    BIT,
    BINARY_REPRESENTATION,
    BINARY_FRACTIONS,
    BITWISE_OPERATION,
    ARITHMETIC_RIGHT_SHIFT,
    HARDWARE,
    COMPUTER,
    COMPUTER_MEMORY,
    CONCURRENCY,
    CORE,
    PARALLELISM,
    PROCESSOR,
    PROGRAM,
    RANDOM_ACCESS_MEMORY,
    RIGHT_SHIFT,
    HEAP_MEMORY,
    HEAP_OVERFLOW,
    LOGICAL_RIGHT_SHIFT,
    STACK_MEMORY,
    CALL_STACK,
    CACHE,
    STACK_OVERFLOW,
    MEMORY_ALLOCATION,
    VARIABLE,
    TWOS_COMPLEMENT,
    ABSTRACT_DATA_TYPE,
    BIT_FIELD,
    COLLECTION,
    MAP,
    PRIMITIVE_DATA_TYPE,
    ASSOCIATIVE_ARRAY,
    HASH_TABLE,
    BAG,
    SET,
    ARRAY,
    LINKED_LIST,
    LIST,
    PRIORITY_QUEUE,
    QUEUE,
    STACK,
    BOOLEAN,
    INTEGER,
    CHARACTER_ENCODING,
    ASCII,
    EXTENDED_ASCII,
    UTF,
    UTF_8,
    UNICODE,
    REGULAR_EXPRESSION,
    STRING,
    SUBSTRING,
    TRIE,
    GRAPH_LABELING,
    GRAPH_COLORING,
    VERTEX_COLORING,
    HASH_COLLISION,
    ROLLING_HASH,
    RABIN_KARP_ALGORITHM,
    BIT_MANIPULATION,
]
