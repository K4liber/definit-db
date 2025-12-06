from definit_db.data.field.mathematics.definitions.fundamental.computation.deterministic_turing_machine import (
    DETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.algorithm.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.problem.algorithm.np_hard_class import NP_HARD_CLASS
from definit_db.data.field.mathematics.definitions.problem.algorithm.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.reduction import REDUCTION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _NPCompleteClass(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a class of {PROBLEM.key.get_reference("problems")} that are both in 
{NP_CLASS.key.get_reference("NP")} and {NP_HARD_CLASS.key.get_reference("NP-Hard")}. A problem is 
NP-Complete if: (1) given a proposed {SOLUTION.key.get_reference()}, it can be verified by a 
{DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")} in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}, and (2) every 
problem in NP can be {REDUCTION.key.get_reference("reduced")} to it in polynomial time. NP-Complete 
problems are the "hardest" problems in NP - if any NP-Complete problem can be solved efficiently, then all 
problems in NP can be solved efficiently. The size of the {INPUT_DATA.key.get_reference()} affects the 
computational difficulty.
"""


NP_COMPLETE_CLASS = _NPCompleteClass(DefinitionKey(name="NP-Complete", field=Field.MATHEMATICS))
