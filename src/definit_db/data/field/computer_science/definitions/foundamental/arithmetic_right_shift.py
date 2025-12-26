from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.foundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.right_shift import RIGHT_SHIFT
from definit_db.data.field.computer_science.definitions.foundamental.twos_complement import TWOS_COMPLEMENT
from definit_db.data.field.mathematics.definitions.fundamental.number.integer import INTEGER


class _ArithmeticRightShift(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {BITWISE_OPERATION.key.get_reference("bitwise operation")} 
and a variant of {RIGHT_SHIFT.key.get_reference("right shift")} that preserves the sign 
{BIT.key.get_reference()} when shifting signed {INTEGER.key.get_reference("integers")}. 
Instead of filling the leftmost positions with zeros, it replicates the sign bit, 
maintaining the correct sign for negative numbers in {TWOS_COMPLEMENT.key.get_reference()} 
representation. This {OPERATION.key.get_reference()} effectively performs signed integer 
division by powers of 2.
"""


ARITHMETIC_RIGHT_SHIFT = _ArithmeticRightShift(
    DefinitionKey(name="arithmetic right shift", field=FieldName.COMPUTER_SCIENCE)
)
