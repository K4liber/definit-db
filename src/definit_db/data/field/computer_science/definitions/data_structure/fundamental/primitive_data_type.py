from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _PrimitiveDataType(Definition):
    def _get_content(self) -> str:
        return f"""
Primitive data types are a {SET.key.get_reference(phrase="set")} of basic 
{DATA_STRUCTURE.key.get_reference(phrase="data structures")} from which all other data types are constructed.
"""


PRIMITIVE_DATA_TYPE = _PrimitiveDataType(
    key=DefinitionKey(
        name="primitive_data_type",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
