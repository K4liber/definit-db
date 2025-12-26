from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _MemoryAllocation(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the {OPERATION.key.get_reference()} of assigning a block of {COMPUTER_MEMORY.key.get_reference()} 
to store {DATA.key.get_reference()} for use by a {PROGRAM.key.get_reference()}. It determines where and how much memory 
is reserved for storing {INFORMATION.key.get_reference()} during program execution.
"""


MEMORY_ALLOCATION = _MemoryAllocation(DefinitionKey(name="memory allocation", field=FieldName.COMPUTER_SCIENCE))
