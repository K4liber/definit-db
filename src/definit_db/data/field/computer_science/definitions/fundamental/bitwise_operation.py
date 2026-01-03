from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION


class _BitwiseOperation(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an {OPERATION.key.get_reference()} that acts on individual {BIT.key.get_reference("bits")} 
within a {BINARY_REPRESENTATION.key.get_reference()}. Bitwise operations work directly on the bits of {DATA.key.get_reference()}, 
allowing for efficient manipulation and comparison at the lowest level of representation.
"""


BITWISE_OPERATION = _BitwiseOperation(DefinitionKey(name="bitwise operation", field=FieldName.COMPUTER_SCIENCE))
