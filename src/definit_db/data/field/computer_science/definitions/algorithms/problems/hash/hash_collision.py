from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.hash_table import (
    HASH_TABLE,
)
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION


class _HashCollision(Definition):
    def _get_content(self) -> str:
        return f"""
A situation in which two different inputs produce the same hash value when processed by a 
{HASH_FUNCTION.key.get_reference(phrase="hash function")}. This can lead to 
{DATA.key.get_reference()} integrity issues and is a key consideration in the design of hash functions and 
{HASH_TABLE.key.get_reference(phrase="hash tables")}.
"""


HASH_COLLISION = _HashCollision(
    key=DefinitionKey(
        name="hash_collision",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
