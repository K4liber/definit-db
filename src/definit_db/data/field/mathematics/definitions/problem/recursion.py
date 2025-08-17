from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Recursion(Definition):
    def _get_content(self) -> str:
        return (
            f"A method of solving a {PROBLEM.key.get_reference()} where the {SOLUTION.key.get_reference()} "
            f"depends on solutions to smaller instances of the same problem. "
            f"Recursion involves a {FUNCTION.key.get_reference()} calling itself with simpler inputs until reaching a "
            f"{BASE_CASE.key.get_reference()}."
        )


RECURSION = _Recursion(
    key=DefinitionKey(
        name="recursion",
        field=Field.MATHEMATICS,
    )
)
