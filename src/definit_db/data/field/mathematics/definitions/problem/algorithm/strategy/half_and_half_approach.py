from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _HalfAndHalfApproach(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} design approach that solves a {PROBLEM.key.get_reference()} by dividing it 
into two equal or nearly equal halves, solving each half independently (often using {RECURSION.key.get_reference()}), 
and then combining the {SOLUTION.key.get_reference("solutions")} from both halves. This approach is particularly 
effective for problems where the {SUBPROBLEM.key.get_reference("subproblems")} can be balanced and 
solved in parallel or sequentially with reduced {COMPLEXITY.key.get_reference()}.
"""


HALF_AND_HALF_APPROACH = _HalfAndHalfApproach(
    key=DefinitionKey(
        name="half_and_half_approach",
        field=FieldName.MATHEMATICS,
    )
)
