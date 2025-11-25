from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _MergeSort(Definition):
    def _get_content(self) -> str:
        return f"""
MergeSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that uses a 
{DIVIDE_AND_CONQUER.key.get_reference()} approach: it divides the input 
{SEQUENCE.key.get_reference("sequence")} into two halves, {RECURSION.key.get_reference("recursively")} sorts each 
half, and then merges the two sorted halves into a single sorted {SEQUENCE.key.get_reference("sequence")}. 
"""


MERGE_SORT = _MergeSort(
    key=DefinitionKey(
        name="merge_sort",
        field=Field.MATHEMATICS,
    )
)
