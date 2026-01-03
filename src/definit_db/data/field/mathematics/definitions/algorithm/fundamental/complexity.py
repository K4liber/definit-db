from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _Complexity(Definition):
    def _get_content(self) -> str:
        return f"""
A measure of the resources required by an {ALGORITHM.key.get_reference()} to solve a 
{PROBLEM.key.get_reference()}, typically expressed as a {FUNCTION.key.get_reference()} of the input size. 
Complexity quantifies how the resource requirements grow as the input size increases, helping to evaluate 
and compare algorithm efficiency.
"""


COMPLEXITY = _Complexity(
    key=DefinitionKey(
        name="complexity",
        field=FieldName.MATHEMATICS,
    )
)
