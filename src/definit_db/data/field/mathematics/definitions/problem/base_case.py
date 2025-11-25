from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.reduction import REDUCTION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _BaseCase(Definition):
    def _get_content(self) -> str:
        return f"""
The simplest instance of the {PROBLEM.key.get_reference()}, which can be 
{SOLUTION.key.get_reference("solved")} directly without further {REDUCTION.key.get_reference()}.
"""


BASE_CASE = _BaseCase(
    key=DefinitionKey(
        name="base_case",
        field=Field.MATHEMATICS,
    )
)
