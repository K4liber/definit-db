from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.primitive_data_type import PRIMITIVE_DATA_TYPE


class _Integer(Definition):
    def _get_content(self) -> str:
        return f"""
A {PRIMITIVE_DATA_TYPE.key.get_reference(phrase="primitive data type")} that represents whole numbers. 
Integers can be positive, negative, or zero.
"""


INTEGER = _Integer(
    key=DefinitionKey(
        name="integer",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
