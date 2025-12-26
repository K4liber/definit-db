from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _OptimalSolution(Definition):
    def _get_content(self) -> str:
        return f"""
A {SOLUTION.key.get_reference(phrase="solution")} that is the best among all possible solutions, often in terms 
of a specific {CRITERION.key.get_reference(phrase="criterion")}.
"""


OPTIMAL_SOLUTION = _OptimalSolution(
    key=DefinitionKey(
        name="optimal_solution",
        field=FieldName.MATHEMATICS,
    )
)
