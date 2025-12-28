from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _BottomUpApproach(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} design approach that constructs {SOLUTION.key.get_reference("solutions")} 
to a {PROBLEM.key.get_reference()} by first solving its smaller {SUBPROBLEM.key.get_reference("subproblems")} 
and then combining those solutions to form a solution to the original problem. The bottom-up approach often avoids 
{RECURSION.key.get_reference()} by iteratively building up answers from the {BASE_CASE.key.get_reference("base cases")}.
"""


BOTTOM_UP_APPROACH = _BottomUpApproach(
    key=DefinitionKey(
        name="bottom_up_approach",
        field=FieldName.MATHEMATICS,
    )
)
