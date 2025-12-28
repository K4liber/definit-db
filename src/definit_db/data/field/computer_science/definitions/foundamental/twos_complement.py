from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.foundamental.bit import BIT
from definit_db.data.field.mathematics.definitions.fundamental.number.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number.number import NUMBER


class _TwosComplement(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a mathematical operation and 
{BINARY_REPRESENTATION.key.get_reference("binary representation")} method used to represent 
signed {INTEGER.key.get_reference("integers")} in computing. In this representation, positive 
{NUMBER.key.get_reference("numbers")} are represented in standard binary form, 
while negative {NUMBER.key.get_reference("numbers")} are represented by inverting all 
{BIT.key.get_reference("bits")} of their positive counterpart and adding 1. 
This method allows both positive and negative {INTEGER.key.get_reference("integers")} to be represented and 
enables arithmetic operations to be performed using the same hardware circuitry, making it the most common method for 
representing signed integers.
"""


TWOS_COMPLEMENT = _TwosComplement(DefinitionKey(name="two's complement", field=FieldName.COMPUTER_SCIENCE))
