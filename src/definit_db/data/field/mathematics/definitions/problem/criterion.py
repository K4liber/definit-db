from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName


class _Criterion(Definition):
    def _get_content(self) -> str:
        return """
A standard or principle by which something is judged or decided.
"""


CRITERION = _Criterion(
    key=DefinitionKey(
        name="criterion",
        field=FieldName.MATHEMATICS,
    )
)
