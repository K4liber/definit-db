from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _PureFunction(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {FUNCTION.key.get_reference()} that always returns the same result 
for the same {INPUT_DATA.key.get_reference("input")}. Pure functions are deterministic and depend only 
on their input values to produce their output values.
"""


PURE_FUNCTION = _PureFunction(DefinitionKey(name="pure function", field=Field.MATHEMATICS))
