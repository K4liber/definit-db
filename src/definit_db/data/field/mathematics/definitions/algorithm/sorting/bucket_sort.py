from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION


class _BucketSort(Definition):
    def _get_content(self) -> str:
        return f"""
BucketSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that distributes the elements of a 
{SEQUENCE.key.get_reference("sequence")} into a number of buckets, sorts each bucket individually (often using 
another {ALGORITHM.key.get_reference()}), and then concatenates the sorted buckets to produce the final sorted 
{SEQUENCE.key.get_reference("sequence")}. Bucket sort can be very efficient when input is uniformly distributed; 
in some cases it can achieve linear time and approach the {OPTIMAL_SOLUTION.key.get_reference("optimal solution")} 
for specific distributions.
"""


BUCKET_SORT = _BucketSort(
    key=DefinitionKey(
        name="bucket_sort",
        field=FieldName.MATHEMATICS,
    )
)
