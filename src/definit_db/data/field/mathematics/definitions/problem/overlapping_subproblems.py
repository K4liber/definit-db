from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _OverlappingSubProblems(Definition):
    def _get_content(self) -> str:
        return f"""
A {PROBLEM.key.get_reference()} is said to have overlapping 
{SUBPROBLEM.key.get_reference(phrase="subproblems")} if the problem can be broken down into smaller, 
simpler subproblems that are reused several times.
"""


OVERLAPPING_SUBPROBLEMS = _OverlappingSubProblems(
    key=DefinitionKey(
        name="overlapping_subproblems",
        field=FieldName.MATHEMATICS,
    )
)
