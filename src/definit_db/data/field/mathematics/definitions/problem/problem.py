from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName


class _Problem(Definition):
    def _get_content(self) -> str:
        return """
A question or a challenge defined in a formal way.
"""


PROBLEM = _Problem(
    key=DefinitionKey(
        name="problem",
        field=FieldName.MATHEMATICS,
    )
)
