from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Sorting(Definition):
    def _get_content(self) -> str:
        return f"""
Sorting is an {ALGORITHM.key.get_reference(phrase="algorithmic")} process that arranges the elements of a 
{SEQUENCE.key.get_reference(phrase="sequence")} or {SET.key.get_reference(phrase="set")} in a certain order, 
typically according to a specified {RELATION.key.get_reference(phrase="relation")} (such as ascending or 
descending). 
"""


SORTING = _Sorting(
    key=DefinitionKey(
        name="sorting",
        field=Field.MATHEMATICS,
    )
)
