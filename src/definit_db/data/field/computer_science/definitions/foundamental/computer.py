from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _Computer(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a device that can execute {INSTRUCTION.key.get_reference("instructions")} 
to process {DATA.key.get_reference("information")} and perform tasks automatically. A computer can store, retrieve, and manipulate 
data according to instructions.
"""


COMPUTER = _Computer(DefinitionKey(name="computer", field=FieldName.COMPUTER_SCIENCE))
