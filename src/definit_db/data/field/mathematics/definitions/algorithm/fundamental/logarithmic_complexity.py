from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.problem.problem_space import PROBLEM_SPACE


class _LogarithmicComplexity(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {TIME_COMPLEXITY.key.get_reference("time complexity")} classification where 
an {ALGORITHM.key.get_reference()} performs a number of {OPERATION.key.get_reference("operations")} that grows 
logarithmically with the size of the {INPUT_DATA.key.get_reference("input")}. Expressed in 
{BIG_O_NOTATION.key.get_reference("Big O notation")} as O(log n), logarithmic complexity means that each 
{OPERATION.key.get_reference()} reduces the {PROBLEM_SPACE.key.get_reference("problem space")} by a constant 
factor (typically by half). This is highly efficient and commonly seen in algorithms that repeatedly divide the problem 
space. Logarithmic complexity is significantly faster than linear complexity, especially for large inputs, as doubling 
the {INPUT_DATA.key.get_reference("input")} size only adds one additional {OPERATION.key.get_reference()}.
"""


LOGARITHMIC_COMPLEXITY = _LogarithmicComplexity(
    DefinitionKey(name="logarithmic complexity", field=FieldName.MATHEMATICS)
)
