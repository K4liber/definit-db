from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION


class _QuickSort(Definition):
    def _get_content(self) -> str:
        return f"""
QuickSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that uses a 
{DIVIDE_AND_CONQUER.key.get_reference()} approach to sort elements. It selects a 'pivot' element, partitions the 
other elements into two sub-{SEQUENCE.key.get_reference("sequences")} according to whether they are less than or 
greater than the pivot, and then {RECURSION.key.get_reference("recursively")} sorts the sub-sequences.
"""


QUICK_SORT = _QuickSort(
    key=DefinitionKey(
        name="quick_sort",
        field=FieldName.MATHEMATICS,
    )
)
