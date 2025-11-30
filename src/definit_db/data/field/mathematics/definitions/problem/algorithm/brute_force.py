from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _BruteForce(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {ALGORITHM.key.get_reference()} that solves a {PROBLEM.key.get_reference()} by systematically checking 
all possible candidates for a {SOLUTION.key.get_reference()} until the correct one is found. Brute force algorithms 
are straightforward and guarantee finding the {OPTIMAL_SOLUTION.key.get_reference("optimal solution")} if one exists, 
but they can be computationally expensive for large problem spaces as they do not employ any {OPTIMIZATION.key.get_reference()} techniques.
"""


BRUTE_FORCE = _BruteForce(
    key=DefinitionKey(
        name="brute_force",
        field=Field.MATHEMATICS,
    )
)
