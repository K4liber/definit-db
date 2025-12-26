from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _HashFunction(Definition):
    def _get_content(self) -> str:
        return f"""
A function that for an input {OBJECT.key.get_reference(phrase="object")} assigns a fixed-size text. 
The text is typically a 'digest' that is unique to each unique input.
"""


HASH_FUNCTION = _HashFunction(
    key=DefinitionKey(
        name="hash_function",
        field=FieldName.MATHEMATICS,
    )
)
