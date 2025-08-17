from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _BucketSort(Definition):
    def _get_content(self) -> str:
        return (
            f"BucketSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that distributes "
            f"the elements of a {SEQUENCE.key.get_reference('sequence')} into a number of buckets, "
            f"sorts each bucket individually (often using another {ALGORITHM.key.get_reference()}), and "
            f"then concatenates the sorted buckets to produce the final sorted {SEQUENCE.key.get_reference('sequence')}. "
            f"Bucket sort can be very efficient when input is uniformly distributed; in some cases it can achieve "
            f"linear time and approach the {OPTIMAL_SOLUTION.key.get_reference('optimal solution')} for specific distributions."
        )


BUCKET_SORT = _BucketSort(
    key=DefinitionKey(
        name="bucket_sort",
        field=Field.MATHEMATICS,
    )
)
