from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.foundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.foundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.number.integer import INTEGER


class _RightShift(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {BITWISE_OPERATION.key.get_reference("bitwise operation")} 
that shifts all {BIT.key.get_reference("bits")} in a 
{BINARY_REPRESENTATION.key.get_reference("binary representation")} to the right by a 
specified number of positions. Right shift by one position is equivalent to 
{INTEGER.key.get_reference()} division by 2.
"""


RIGHT_SHIFT = _RightShift(DefinitionKey(name="right shift", field=FieldName.COMPUTER_SCIENCE))
