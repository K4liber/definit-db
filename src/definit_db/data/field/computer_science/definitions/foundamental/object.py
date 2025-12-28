from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.data_structure import DATA_STRUCTURE


class _Object(Definition):
    def _get_content(self) -> str:
        return f"""
An object is an instance of a {DATA_STRUCTURE.key.get_reference(phrase="data structure")}.
"""


OBJECT = _Object(
    key=DefinitionKey(
        name="object",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
