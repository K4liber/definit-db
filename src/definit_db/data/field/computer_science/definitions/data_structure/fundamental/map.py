from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE


class _Map(Definition):
    def _get_content(self) -> str:
        return f"""
A {DATA_STRUCTURE.key.get_reference(phrase="data structure")} that maps keys to values. Each key can map to at 
most one value. It models the mathematical function abstraction.
"""


MAP = _Map(
    key=DefinitionKey(
        name="map",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
