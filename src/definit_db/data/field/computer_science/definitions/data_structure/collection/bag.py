from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.multiset import MULTISET


class _Bag(Definition):
    def _get_content(self) -> str:
        return f"""
A bag is a {COLLECTION.key.get_reference(phrase="collection")} that allows for the storage of multiple items, 
where the same item can be stored multiple times. It is similar to a 
{MULTISET.key.get_reference(phrase="multiset")}, but does not require any specific ordering of the items. Removing 
items is not supported. A bag allows to iterate through the collected items.
"""


BAG = _Bag(
    key=DefinitionKey(
        name="bag",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
