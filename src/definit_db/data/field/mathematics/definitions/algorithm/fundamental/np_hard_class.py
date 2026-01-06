from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.reduction import REDUCTION


class _NPHardClass(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a class of {PROBLEM.key.get_reference("problems")} in computational 
complexity theory that are at least as hard as the hardest problems in {NP_CLASS.key.get_reference("NP")}. 
A problem is NP-Hard if every problem in NP can be {REDUCTION.key.get_reference("reduced")} to it in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}. This means that 
if we had an {ALGORITHM.key.get_reference()} to solve an NP-Hard problem efficiently, we could use it to 
solve all NP problems efficiently. NP-Hard problems are not necessarily in NP themselves - they may be even 
harder, with no way to verify solutions quickly. The {REDUCTION.key.get_reference()} is used as a 
theoretical tool to prove hardness, not to solve problems. The size of the {INPUT_DATA.key.get_reference()} 
determines the complexity of solving NP-Hard problems.
"""


NP_HARD_CLASS = _NPHardClass(DefinitionKey(name="NP-Hard class", field=FieldName.MATHEMATICS))
