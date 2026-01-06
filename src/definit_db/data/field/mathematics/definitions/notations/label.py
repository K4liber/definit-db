from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Label(Definition):
    def _get_content(self) -> str:
        return f"""
A label is a name, number, or symbol attached to an {OBJECT.key.get_reference(phrase="object")} to give it 
meaning or identify it.
"""


LABEL = _Label(
    key=DefinitionKey(
        name="label",
        field=FieldName.MATHEMATICS,
    )
)
