from definit_db.data.field.computer_science.definitions.foundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.foundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.foundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.right_shift import RIGHT_SHIFT
from definit_db.data.field.mathematics.definitions.fundamental.number.integer import INTEGER
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _LogicalRightShift(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {BITWISE_OPERATION.key.get_reference("bitwise operation")} 
and a variant of {RIGHT_SHIFT.key.get_reference("right shift")} that always fills the 
leftmost {BIT.key.get_reference("bits")} with zeros, regardless of the sign of the 
{INTEGER.key.get_reference()}. This {OPERATION.key.get_reference()} treats the 
{BINARY_REPRESENTATION.key.get_reference("binary representation")} as an unsigned value, 
making it suitable for unsigned integer division by powers of 2.
"""


LOGICAL_RIGHT_SHIFT = _LogicalRightShift(DefinitionKey(name="logical right shift", field=Field.COMPUTER_SCIENCE))
