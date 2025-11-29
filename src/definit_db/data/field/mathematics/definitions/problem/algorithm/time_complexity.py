from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.complexity import COMPLEXITY
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _TimeComplexity(Definition):
    def _get_content(self) -> str:
        return f"""
A measure of {COMPLEXITY.key.get_reference()} that quantifies the amount of time an 
{ALGORITHM.key.get_reference()} takes to complete as a {FUNCTION.key.get_reference()} of the input size. 
Time complexity describes how the number of operations or execution time grows with increasing input size.
"""


TIME_COMPLEXITY = _TimeComplexity(
    key=DefinitionKey(
        name="time_complexity",
        field=Field.MATHEMATICS,
    )
)
