from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _AsymptoticBehavior(Definition):
    def _get_content(self) -> str:
        return f"""
The behavior of a {FUNCTION.key.get_reference()} as its input approaches infinity or some other limit value. 
Asymptotic behavior describes how a function grows or behaves in the limit, focusing on the dominant terms and 
ignoring lower-order terms and constant factors.
"""


ASYMPTOTIC_BEHAVIOR = _AsymptoticBehavior(
    key=DefinitionKey(
        name="asymptotic_behavior",
        field=Field.MATHEMATICS,
    )
)
