from definit_db.data.field.computer_science.definitions.foundamental.bit import BIT
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.number.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _BinaryRepresentation(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a way of expressing {INFORMATION.key.get_reference()} using only two symbols, typically 0 and 1. 
In this system, each digit is called a {BIT.key.get_reference()}, and {SEQUENCE.key.get_reference("sequences")} of bits are used to represent {NUMBER.key.get_reference("numbers")} 
and other types of information.
"""


BINARY_REPRESENTATION = _BinaryRepresentation(DefinitionKey(name="binary representation", field=Field.COMPUTER_SCIENCE))
