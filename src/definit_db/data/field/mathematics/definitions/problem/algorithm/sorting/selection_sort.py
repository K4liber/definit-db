from definit_db.data.field.mathematics.definitions.foundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _SelectionSort(Definition):
    def _get_content(self) -> str:
        return (
            f"SelectionSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that sorts an "
            f"{SEQUENCE.key.get_reference('sequence')} by repeatedly finding the minimum (or maximum) element from the "
            f"unsorted part and moving it to the beginning (or end). This process is repeated until the entire "
            f"sequence is sorted."
        )


SELECTION_SORT = _SelectionSort(
    key=DefinitionKey(
        name="selection_sort",
        field=Field.MATHEMATICS,
    )
)
