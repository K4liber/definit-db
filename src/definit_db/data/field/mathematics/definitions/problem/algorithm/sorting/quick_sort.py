from definit_db.data.field.mathematics.definitions.foundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _QuickSort(Definition):
    def _get_content(self) -> str:
        return (
            f"QuickSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that uses a "
            f"{DIVIDE_AND_CONQUER.key.get_reference()} approach to sort elements. It selects a 'pivot' element, "
            f"partitions the other elements into two sub-{SEQUENCE.key.get_reference('sequences')} according to "
            f"whether they are less than or greater than the pivot, and then "
            f"{RECURSION.key.get_reference('recursively')} sorts the sub-sequences."
        )


QUICK_SORT = _QuickSort(
    key=DefinitionKey(
        name="quick_sort",
        field=Field.MATHEMATICS,
    )
)
