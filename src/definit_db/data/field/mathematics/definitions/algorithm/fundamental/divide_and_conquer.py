from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _DivideAndConquer(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {ALGORITHM.key.get_reference()} that solves a {PROBLEM.key.get_reference()} by 
{RECURSION.key.get_reference("recursively")} breaking it down into smaller 
{SUBPROBLEM.key.get_reference("subproblems")}, solving each subproblem independently, and then combining their 
{SOLUTION.key.get_reference("solutions")} to form a solution to the original problem. Divide and conquer 
algorithms often lead to efficient and elegant solutions. They may or may not always produce the 
{OPTIMAL_SOLUTION.key.get_reference("optimal solution")}.
"""


DIVIDE_AND_CONQUER = _DivideAndConquer(
    key=DefinitionKey(
        name="divide_and_conquer",
        field=FieldName.MATHEMATICS,
    )
)
