from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _ProblemSpace(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the {SET.key.get_reference()} of all possible candidates for 
{SOLUTION.key.get_reference("solutions")} to a {PROBLEM.key.get_reference()}. It represents the entire 
domain that must be searched through to find a valid or {OPTIMAL_SOLUTION.key.get_reference("optimal solution")}. 
The size of the problem space directly impacts computational efficiency, as larger problem spaces typically require 
more computational resources to explore.
"""


PROBLEM_SPACE = _ProblemSpace(DefinitionKey(name="problem space", field=Field.MATHEMATICS))
