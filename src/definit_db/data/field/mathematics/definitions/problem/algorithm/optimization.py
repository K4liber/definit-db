from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Optimization(Definition):
    def _get_content(self) -> str:
        return f"""
The process of improving an {ALGORITHM.key.get_reference()} or {SOLUTION.key.get_reference()} to make it more 
efficient by reducing resource consumption. {self.key.get_reference()} 
involves finding the best approach to solve a {PROBLEM.key.get_reference()} within given {CONSTRAINT.key.get_reference("constraints")}, often by 
minimizing costs or maximizing benefits.
"""


OPTIMIZATION = _Optimization(
    key=DefinitionKey(
        name="optimization",
        field=Field.MATHEMATICS,
    )
)
