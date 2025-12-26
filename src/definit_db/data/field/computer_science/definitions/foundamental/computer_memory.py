from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.computer_science.definitions.foundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _ComputerMemory(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {HARDWARE.key.get_reference()} component that stores {DATA.key.get_reference()} for immediate use 
by a {COMPUTER.key.get_reference()}. It provides storage for {INSTRUCTION.key.get_reference("instructions")} and data that are actively being processed or accessed, 
enabling the computer to perform {OPERATION.key.get_reference("operations")} efficiently.
"""


COMPUTER_MEMORY = _ComputerMemory(DefinitionKey(name="computer memory", field=FieldName.COMPUTER_SCIENCE))
