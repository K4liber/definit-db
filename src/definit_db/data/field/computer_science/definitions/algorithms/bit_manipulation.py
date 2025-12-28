from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.foundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.foundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM


class _BitManipulation(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a technique that uses {BITWISE_OPERATION.key.get_reference("bitwise operations")} to perform direct operations 
on individual {BIT.key.get_reference("bits")} or groups of bits in a {BINARY_REPRESENTATION.key.get_reference()}. 
It is commonly used in {ALGORITHM.key.get_reference("algorithms")} for tasks like setting, clearing, toggling, 
or checking specific bits, as well as performing efficient computations.
"""


BIT_MANIPULATION = _BitManipulation(DefinitionKey(name="bit manipulation", field=FieldName.COMPUTER_SCIENCE))
