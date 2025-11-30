from definit_db.data.field.computer_science.definitions.foundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.computer_science.definitions.foundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.foundamental.program import PROGRAM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _HeapMemory(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a region of {COMPUTER_MEMORY.key.get_reference()} used for dynamic {MEMORY_ALLOCATION.key.get_reference()} 
during {PROGRAM.key.get_reference()} execution. It allows {DATA.key.get_reference()} to be allocated and deallocated 
at runtime as needed. The heap provides flexible memory management where 
memory blocks can be allocated in any order and freed in any order.
"""


HEAP_MEMORY = _HeapMemory(DefinitionKey(name="heap memory", field=Field.COMPUTER_SCIENCE))
