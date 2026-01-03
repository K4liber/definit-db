from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.abstract_data_type import (
    ABSTRACT_DATA_TYPE,
)
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION


class _Collection(Definition):
    def _get_content(self) -> str:
        return f"""
Collection is an {ABSTRACT_DATA_TYPE.key.get_reference(phrase="abstract data type")} that groups some variable 
number of {DATA_STRUCTURE.key.get_reference(phrase="data structures")} (possibly zero) that have some shared 
significance to the problem being solved and need to be {OPERATION.key.get_reference(phrase="operated")} upon 
together in some controlled fashion.
"""


COLLECTION = _Collection(
    key=DefinitionKey(
        name="collection",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
