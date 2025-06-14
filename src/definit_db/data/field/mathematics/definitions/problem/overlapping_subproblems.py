from definit_db.data.field.mathematics.definitions.problem.algorithm.subproblem import SUBPROBLEM
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _OverlappingSubProblems(Definition):
    def _get_content(self) -> str:
        return (
            f"A {PROBLEM.key.get_reference()} is said to have overlapping "
            f"{SUBPROBLEM.key.get_reference(phrase='subproblems')} if the problem can be broken down into smaller, "
            "simpler subproblems that are reused several times."
        )


OVERLAPPING_SUBPROBLEMS = _OverlappingSubProblems(
    key=DefinitionKey(
        name="overlapping_subproblems",
        field=Field.MATHEMATICS,
    )
)
