from definit_db.data.field.mathematics.definitions.number.number import NUMBER
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Integer(Definition):
    def _get_content(self) -> str:
        return f"""
An integer is the {NUMBER.key.get_reference()} zero (0), a positive natural number (1, 2, 3, ...), or the 
negation of a positive natural number (-1, -2, -3, ...). The negations or additive inverses of the positive 
natural numbers are referred to as negative integers.
"""


INTEGER = _Integer(
    key=DefinitionKey(
        name="integer",
        field=Field.MATHEMATICS,
    )
)
