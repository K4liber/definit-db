from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.number.integer import INTEGER
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _RadixSort(Definition):
    def _get_content(self) -> str:
        return (
            f"Radix Sort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that sorts "
            f"a {SEQUENCE.key.get_reference('sequence')} of {INTEGER.key.get_reference('integers')} "
            f"(or other {OBJECT.key.get_reference(phrase='objects')} that can be represented by integers) by processing individual "
            f"digits or positions of the keys, grouping elements by each digit from least significant to most (LSD) "
            f"or most to least significant (MSD). It is a non-comparative sorting technique: instead of comparing "
            f"elements directly, it distributes them into buckets according to the value of the current digit and then "
            f"collects them in order. When the number of digits (or key range per digit) is bounded, radix sort can "
            f"run in linear time with respect to the number of elements and thus approach the "
            f"{OPTIMAL_SOLUTION.key.get_reference('optimal solution')} "
            f"for those inputs."
        )


RADIX_SORT = _RadixSort(
    key=DefinitionKey(
        name="radix_sort",
        field=Field.MATHEMATICS,
    )
)
