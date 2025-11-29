from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.overlapping_subproblems import OVERLAPPING_SUBPROBLEMS
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _TopDownApproach(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} design approach that breaks a {PROBLEM.key.get_reference()} into smaller
{SUBPROBLEM.key.get_reference("subproblems")} and solves them using {RECURSION.key.get_reference()}. The top-down
approach typically stores results of subproblems when the problem exhibits 
{OVERLAPPING_SUBPROBLEMS.key.get_reference()}, avoiding redundant work and building solutions 
from those stored results.
"""


TOP_DOWN_APPROACH = _TopDownApproach(
    key=DefinitionKey(
        name="top_down_approach",
        field=Field.MATHEMATICS,
    )
)
