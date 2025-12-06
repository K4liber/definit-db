from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _ComplementProblem(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of a decision {PROBLEM.key.get_reference()} is obtained by swapping 
the "yes" and "no" answers. If the original problem accepts a {SOLUTION.key.get_reference()} as "yes", 
the complement problem answers "no" for the same solution, and vice versa. For example, if a problem 
asks "Is this graph connected?", its complement asks "Is this graph disconnected?". The complement 
inverts the acceptance {CRITERION.key.get_reference("criteria")} while keeping the same 
{INPUT_DATA.key.get_reference("input")} structure.
"""


COMPLEMENT_PROBLEM = _ComplementProblem(DefinitionKey(name="complement problem", field=Field.MATHEMATICS))
