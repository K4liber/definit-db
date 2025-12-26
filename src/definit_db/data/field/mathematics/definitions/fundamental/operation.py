from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Operation(Definition):
    def _get_content(self) -> str:
        return f"""
A mathematical action performed on one or more {OBJECT.key.get_reference(phrase="objects")} to produce a result.
"""


OPERATION = _Operation(
    key=DefinitionKey(
        name="operation",
        field=FieldName.MATHEMATICS,
    )
)
