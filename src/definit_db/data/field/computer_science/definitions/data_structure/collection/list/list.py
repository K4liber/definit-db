from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.fundamental.data_type import DATA_TYPE


class _List(Definition):
    def _get_content(self) -> str:
        return f"""
An ordered {COLLECTION.key.get_reference(phrase="collection")}. Also known as a sequence. One can add, remove, and 
pop any element from the list. List can store elements of different {DATA_TYPE.key.get_reference(phrase="types")}.
"""


LIST = _List(
    key=DefinitionKey(
        name="list",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
