from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Set(Definition):
    def _get_content(self) -> str:
        return f"""
Set is a group of different things. These things are called elements or members of the set and are typically 
mathematical {OBJECT.key.get_reference(phrase="objects")} of any kind.
"""


SET = _Set(
    key=DefinitionKey(
        name="set",
        field=FieldName.MATHEMATICS,
    )
)
