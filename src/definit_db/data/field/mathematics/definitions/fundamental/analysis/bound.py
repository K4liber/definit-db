from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Bound(Definition):
    def _get_content(self) -> str:
        return f"""
A limit on the values that a {FUNCTION.key.get_reference()} or expression can take. A bound constrains or 
restricts the range or growth of values, providing a reference point for comparison.
"""


BOUND = _Bound(
    key=DefinitionKey(
        name="bound",
        field=Field.MATHEMATICS,
    )
)
