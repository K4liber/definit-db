from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.fundamental.analysis.upper_bound import UPPER_BOUND
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.algorithm.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.algorithm.time_complexity import TIME_COMPLEXITY


class _BigONotation(Definition):
    def _get_content(self) -> str:
        return f"""
A mathematical notation used to describe the {ASYMPTOTIC_BEHAVIOR.key.get_reference()} of a 
{FUNCTION.key.get_reference()}, particularly the {UPPER_BOUND.key.get_reference()} of 
{TIME_COMPLEXITY.key.get_reference()} or {SPACE_COMPLEXITY.key.get_reference()} as the input size grows. 
Big O notation characterizes the worst-case growth rate, allowing comparison of algorithm efficiency 
independent of implementation details.
"""


BIG_O_NOTATION = _BigONotation(
    key=DefinitionKey(
        name="big_o_notation",
        field=FieldName.MATHEMATICS,
    )
)
