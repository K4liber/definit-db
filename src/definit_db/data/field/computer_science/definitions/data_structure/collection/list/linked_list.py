from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _LinkedList(Definition):
    def _get_content(self) -> str:
        return f"""
An ordered {COLLECTION.key.get_reference(phrase="collection")} of elements. Each element is stored in a 
{NODE.key.get_reference(phrase="node")} that contains a reference to the next node in the list. Linked lists can 
be singly linked or doubly linked, depending on whether each node has a reference to the next node only or both the 
next and previous nodes.
"""


LINKED_LIST = _LinkedList(
    key=DefinitionKey(
        name="linked_list",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
