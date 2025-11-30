from definit_db.data.field.computer_science.definitions.foundamental.heap_memory import HEAP_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.foundamental.program import PROGRAM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _HeapOverflow(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} occurs when a {PROGRAM.key.get_reference()} attempts to use more {HEAP_MEMORY.key.get_reference()} 
than is available. This typically happens when too much dynamic {MEMORY_ALLOCATION.key.get_reference()} occurs without 
proper deallocation, or when attempting to allocate a very large amount of memory at once. When heap overflow occurs, 
the program may fail to allocate memory and typically terminates with an error.
"""


HEAP_OVERFLOW = _HeapOverflow(DefinitionKey(name="heap overflow", field=Field.COMPUTER_SCIENCE))
