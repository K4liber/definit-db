from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION


class _Function(Definition):
    def _get_content(self) -> str:
        return f"""
Function it is a kind of {RELATION.key.get_reference(phrase="relation")} which from a set X to a set Y 
assigns to each element (or {OBJECT.key.get_reference(phrase="object")}) of X exactly one element of Y.
"""


FUNCTION = _Function(
    key=DefinitionKey(
        name="function",
        field=FieldName.MATHEMATICS,
    )
)
