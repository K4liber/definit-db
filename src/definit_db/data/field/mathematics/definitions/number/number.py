from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Number(Definition):
    def _get_content(self) -> str:
        return f"A number is a mathematical {OBJECT.key.get_reference()} used to count, measure, and label."


NUMBER = _Number(
    key=DefinitionKey(
        name="number",
        field=Field.MATHEMATICS,
    )
)
