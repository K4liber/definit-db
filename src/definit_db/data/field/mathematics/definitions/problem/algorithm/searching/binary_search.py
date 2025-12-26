from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING


class _BinarySearch(Definition):
    def _get_content(self) -> str:
        return f"""
Binary Search is an {ALGORITHM.key.get_reference()} that finds the position of a target value 
within a {SEQUENCE.key.get_reference("sequence")} by repeatedly dividing the search interval in half. 
Binary search requires the {SEQUENCE.key.get_reference("sequence")} to be {SORTING.key.get_reference(phrase="sorted")}. 
At each step it compares the target with the middle element of the interval and then continues 
the search on the left or right half, effectively using a {DIVIDE_AND_CONQUER.key.get_reference()} approach.
"""


BINARY_SEARCH = _BinarySearch(
    key=DefinitionKey(
        name="binary_search",
        field=FieldName.MATHEMATICS,
    )
)
