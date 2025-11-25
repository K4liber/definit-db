from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Operation(Definition):
    def _get_content(self) -> str:
        return f"""
A mathematical action performed on one or more {OBJECT.key.get_reference(phrase="objects")} to produce a result.
"""


OPERATION = _Operation(
    key=DefinitionKey(
        name="operation",
        field=Field.MATHEMATICS,
    )
)
