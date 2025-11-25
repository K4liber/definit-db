from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _GreedyAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {ALGORITHM.key.get_reference()} that builds up a {SOLUTION.key.get_reference()} piece by piece, always 
choosing the next piece that offers the most immediate benefit. Greedy algorithms do not always produce the 
{OPTIMAL_SOLUTION.key.get_reference("optimal solution")}, but they are often faster and simpler than other 
approaches.
"""


GREEDY_ALGORITHM = _GreedyAlgorithm(
    key=DefinitionKey(
        name="greedy_algorithm",
        field=Field.MATHEMATICS,
    )
)
