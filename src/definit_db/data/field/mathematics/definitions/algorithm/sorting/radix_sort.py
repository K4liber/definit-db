from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.radix import RADIX
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION


class _RadixSort(Definition):
    def _get_content(self) -> str:
        return f"""
{RADIX.key.get_reference("Radix")} Sort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that sorts 
a {SEQUENCE.key.get_reference("sequence")} of {INTEGER.key.get_reference("integers")} 
(or other {OBJECT.key.get_reference(phrase="objects")} that can be represented by integers) by processing individual 
digits or positions of the keys, grouping elements by each digit from least significant to most (LSD) 
or most to least significant (MSD). It is a non-comparative sorting technique: instead of comparing 
elements directly, it distributes them into buckets according to the value of the current digit and then 
collects them in order. When the number of digits (or key range per digit) is bounded, radix sort can 
run in linear time with respect to the number of elements and thus approach the 
{OPTIMAL_SOLUTION.key.get_reference("optimal solution")} 
for those inputs."
"""


RADIX_SORT = _RadixSort(
    key=DefinitionKey(
        name="radix_sort",
        field=FieldName.MATHEMATICS,
    )
)
