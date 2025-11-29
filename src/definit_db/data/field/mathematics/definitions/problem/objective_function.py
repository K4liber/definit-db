from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _ObjectiveFunction(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {FUNCTION.key.get_reference()} that represents the goal or objective 
to be optimized in a {PROBLEM.key.get_reference()}. The objective function is either maximized or minimized 
to find the best solution, and its value determines the quality of any given solution.
"""


OBJECTIVE_FUNCTION = _ObjectiveFunction(DefinitionKey(name="objective function", field=Field.MATHEMATICS))
