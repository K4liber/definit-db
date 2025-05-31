from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.subproblem import SUBPROBLEM
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _DivideAndConquer(Definition):
    def _get_content(self) -> str:
        return (
            f"A type of {ALGORITHM.key.get_reference()} that solves a {PROBLEM.key.get_reference()} by "
            f"{RECURSION.key.get_reference('recursively')} breaking it down into smaller "
            f"{SUBPROBLEM.key.get_reference('subproblems')}, solving each subproblem independently, "
            f"and then combining their {SOLUTION.key.get_reference('solutions')} "
            "to form a solution to the original problem. "
            f"Divide and conquer algorithms often lead to efficient and elegant solutions. "
            f"They may or may not always produce the {OPTIMAL_SOLUTION.key.get_reference('optimal solution')}."
        )


DIVIDE_AND_CONQUER = _DivideAndConquer(
    key=DefinitionKey(
        name="divide_and_conquer",
        field=Field.MATHEMATICS,
    )
)
