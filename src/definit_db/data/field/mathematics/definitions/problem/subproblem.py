from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _Subproblem(Definition):
    def _get_content(self) -> str:
        return f"""
A smaller, more manageable {PROBLEM.key.get_reference(phrase="problem")} derived from a larger problem, often 
used in the context of problem-solving and algorithm design.
"""


SUBPROBLEM = _Subproblem(
    key=DefinitionKey(
        name="subproblem",
        field=FieldName.MATHEMATICS,
    )
)
