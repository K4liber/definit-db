from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Set(Definition):
    def _get_content(self) -> str:
        return f"Set is a group of different things. These things are called elements or members of the set and are typically mathematical {OBJECT.key.get_reference(phrase='objects')} of any kind."


SET = _Set(
    key=DefinitionKey(
        name="set",
        field=Field.MATHEMATICS,
    )
)
