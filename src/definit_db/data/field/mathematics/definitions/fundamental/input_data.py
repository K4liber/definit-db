from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _InputData(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is the {INFORMATION.key.get_reference()} provided to a 
{FUNCTION.key.get_reference()} to be processed. 
It represents the initial state or values that the function operates on to produce an output.
"""


INPUT_DATA = _InputData(DefinitionKey(name="input data", field=Field.MATHEMATICS))
