from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.notations.label import LABEL


class _Variable(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a named storage location identified by a {LABEL.key.get_reference()} 
that holds {DATA.key.get_reference()} which can be modified during program execution. 
A variable associates a name with a value that can change over time.
"""


VARIABLE = _Variable(DefinitionKey(name="variable", field=FieldName.COMPUTER_SCIENCE))
