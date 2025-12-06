from definit_db.data.field.mathematics.definitions.fundamental.computation.deterministic_turing_machine import (
    DETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.problem.algorithm.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.algorithm.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _PClass(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {COMPLEXITY.key.get_reference("complexity")} class in computational 
complexity theory that contains all decision {PROBLEM.key.get_reference("problems")} that can be solved 
by a {DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")} in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time complexity")}. 
A problem is in P if there exists an {ALGORITHM.key.get_reference()} that can solve any instance of the 
problem in time {BIG_O_NOTATION.key.get_reference("O(n^k)")} for some constant k, where n is the size 
of the {INPUT_DATA.key.get_reference()}. Problems in P are considered efficiently solvable or tractable.
"""


P_CLASS = _PClass(DefinitionKey(name="P", field=Field.MATHEMATICS))
