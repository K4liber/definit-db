from definit_db.data.field.computer_science.definitions.foundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.foundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Processor(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {HARDWARE.key.get_reference()} component of a {COMPUTER.key.get_reference()} 
that executes {INSTRUCTION.key.get_reference("instructions")} and performs {OPERATION.key.get_reference("operations")} 
on data. It is the central component responsible for carrying out the computational tasks defined by {PROGRAM.key.get_reference("programs")}, 
often referred to as the central processing unit (CPU).
"""


PROCESSOR = _Processor(DefinitionKey(name="processor", field=Field.COMPUTER_SCIENCE))
