from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _BubbleSort(Definition):
    def _get_content(self) -> str:
        return (
            f"Bubble Sort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that repeatedly\n"
            f"steps through a {SEQUENCE.key.get_reference('sequence')}, compares adjacent elements and swaps them if\n"
            f"they are in the wrong order. This process is repeated until the entire "
            f"{SEQUENCE.key.get_reference('sequence')} is sorted. "
            f"Bubble sort is simple but generally inefficient for large inputs, as it repeatedly passes\n"
            f"over the sequence."
        )


BUBBLE_SORT = _BubbleSort(
    key=DefinitionKey(
        name="bubble_sort",
        field=Field.MATHEMATICS,
    )
)
