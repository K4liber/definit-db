from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _FeasibleSolution(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {SOLUTION.key.get_reference()} to a {PROBLEM.key.get_reference()} 
that satisfies all the {CONSTRAINT.key.get_reference("constraints")}. A feasible solution may not be optimal, 
but it meets all the requirements and restrictions of the problem.
"""


FEASIBLE_SOLUTION = _FeasibleSolution(DefinitionKey(name="feasible solution", field=Field.MATHEMATICS))
