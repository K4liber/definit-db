from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA


class _DataStructure(Definition):
    def _get_content(self) -> str:
        return f"""
A data structure is a way of organizing and storing {DATA.key.get_reference(phrase="data")} so it can be accessed 
and modified efficiently. A data structure contains a value or group of values and the functions or operations 
that can be applied to the data.
"""


DATA_STRUCTURE = _DataStructure(
    key=DefinitionKey(
        name="data_structure",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
