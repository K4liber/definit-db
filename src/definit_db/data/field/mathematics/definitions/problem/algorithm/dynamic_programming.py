from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.subproblem import SUBPROBLEM
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.optimal_substructure import OPTIMAL_SUBSTRUCTURE
from definit_db.data.field.mathematics.definitions.problem.overlapping_subproblems import OVERLAPPING_SUBPROBLEMS
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _DynamicProgramming(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {ALGORITHM.key.get_reference()} that solves a {PROBLEM.key.get_reference()} by breaking it down into 
simpler {SUBPROBLEM.key.get_reference("subproblems")} and storing their {SOLUTION.key.get_reference("solutions")} 
to avoid redundant computations. Dynamic programming is particularly effective for problems that exhibit 
{OVERLAPPING_SUBPROBLEMS.key.get_reference()} and {OPTIMAL_SUBSTRUCTURE.key.get_reference()}, enabling the 
construction of an {OPTIMAL_SOLUTION.key.get_reference("optimal solution")} by reusing previously computed results.
"""


DYNAMIC_PROGRAMMING = _DynamicProgramming(
    key=DefinitionKey(
        name="dynamic_programming",
        field=Field.MATHEMATICS,
    )
)
