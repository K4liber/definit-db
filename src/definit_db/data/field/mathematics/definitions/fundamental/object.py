from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName


class _Object(Definition):
    def _get_content(self) -> str:
        return """
An object is an abstract concept arising in mathematics. 
Typically, a mathematical object can be a value that can be assigned to a symbol.
"""


OBJECT = _Object(
    key=DefinitionKey(
        name="object",
        field=FieldName.MATHEMATICS,
    )
)
