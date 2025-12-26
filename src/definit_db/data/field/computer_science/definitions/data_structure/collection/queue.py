from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.collection import COLLECTION
from definit_db.data.field.computer_science.definitions.foundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION


class _Queue(Definition):
    def _get_content(self) -> str:
        return f"""
Queue is a {DATA_STRUCTURE.key.get_reference(phrase="data structure")} providing first-in-first-out (FIFO) 
semantics. Serves as a {COLLECTION.key.get_reference(phrase="collection")} of elements with two main 
{OPERATION.key.get_reference(phrase="operations")}:
- Enqueue, which adds an element to the rear of the queue, and
- Dequeue, which removes an element from the front.
Additionally, a peek {OPERATION.key.get_reference(phrase="operation")} can, without modifying the queue, return 
the value of the next element to be dequeued without dequeuing it.
"""


QUEUE = _Queue(
    key=DefinitionKey(
        name="queue",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
