from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.computation.deterministic_turing_machine import (
    DETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.fundamental.computation.nondeterministic_turing_machine import (
    NONDETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.algorithm.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.problem.algorithm.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.algorithm.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.problem.algorithm.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.complement_problem import COMPLEMENT_PROBLEM
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _CoNPClass(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {COMPLEXITY.key.get_reference("complexity")} class in computational 
complexity theory that contains all decision {PROBLEM.key.get_reference("problems")} whose 
{COMPLEMENT_PROBLEM.key.get_reference("complement")} is in {NP_CLASS.key.get_reference("NP")}. A 
problem is in Co-NP if the "no" instances can be verified by a 
{DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")} in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time complexity")}. 
Equivalently, the {COMPLEMENT_PROBLEM.key.get_reference("complement")} of the problem can be solved by a 
{NONDETERMINISTIC_TURING_MACHINE.key.get_reference("nondeterministic Turing machine")} in time 
{BIG_O_NOTATION.key.get_reference("O(n^k)")} for some constant k, where n is the size of the 
{INPUT_DATA.key.get_reference()}. Co-NP stands for "Complement of NP."
"""


CO_NP_CLASS = _CoNPClass(DefinitionKey(name="Co-NP", field=FieldName.MATHEMATICS))
