from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Program(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {SEQUENCE.key.get_reference()} of {INSTRUCTION.key.get_reference("instructions")} that a {COMPUTER.key.get_reference()} 
can execute to perform a specific task. A program defines the {OPERATION.key.get_reference("operations")} that should be carried out and 
the order in which they should be executed.
"""


PROGRAM = _Program(DefinitionKey(name="program", field=FieldName.COMPUTER_SCIENCE))
