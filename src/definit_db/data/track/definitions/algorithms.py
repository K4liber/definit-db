from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.graph_coloring import (
    GRAPH_COLORING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.graph_labeling import (
    GRAPH_LABELING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.vertex_coloring import (
    VERTEX_COLORING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.hash_collision import HASH_COLLISION
from definit_db.data.field.computer_science.definitions.algorithms.problems.rolling_hash import ROLLING_HASH
from definit_db.data.field.computer_science.definitions.algorithms.searching.string.rabin_karp_algorithm import (
    RABIN_KARP_ALGORITHM,
)
from definit_db.data.field.mathematics.definitions.fundamental.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.fundamental.analysis.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.analysis.upper_bound import UPPER_BOUND
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.merge import MERGE
from definit_db.data.field.mathematics.definitions.fundamental.notations.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.uniform_distribution import UNIFORM_DISTRIBUTION
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.brute_force import BRUTE_FORCE
from definit_db.data.field.mathematics.definitions.problem.algorithm.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.algorithm.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.problem.algorithm.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.problem.algorithm.greedy_algorithm import GREEDY_ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.searching.binary_search import BINARY_SEARCH
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.bubble_sort import BUBBLE_SORT
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.bucket_sort import BUCKET_SORT
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.heap_sort import HEAP_SORT
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.merge_sort import MERGE_SORT
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.quick_sort import QUICK_SORT
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.radix_sort import RADIX_SORT
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.selection_sort import SELECTION_SORT
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.problem.algorithm.sorting.topological_sort import TOPOLOGICAL_SORT
from definit_db.data.field.mathematics.definitions.problem.algorithm.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.algorithm.strategy.bottom_up_approach import (
    BOTTOM_UP_APPROACH,
)
from definit_db.data.field.mathematics.definitions.problem.algorithm.strategy.half_and_half_approach import (
    HALF_AND_HALF_APPROACH,
)
from definit_db.data.field.mathematics.definitions.problem.algorithm.strategy.top_down_approach import TOP_DOWN_APPROACH
from definit_db.data.field.mathematics.definitions.problem.algorithm.subproblem import SUBPROBLEM
from definit_db.data.field.mathematics.definitions.problem.algorithm.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.optimal_substructure import OPTIMAL_SUBSTRUCTURE
from definit_db.data.field.mathematics.definitions.problem.overlapping_subproblems import OVERLAPPING_SUBPROBLEMS
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.reduction import REDUCTION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.track.definitions.track_definitions_abstract import TrackDefinitionsAbstract
from definit_db.definition.definition_key import DefinitionKey

_definition_keys: tuple[DefinitionKey, ...] = (
    PROBLEM.key,
    CRITERION.key,
    OPTIMAL_SOLUTION.key,
    OPTIMAL_SUBSTRUCTURE.key,
    SOLUTION.key,
    SUBPROBLEM.key,
    ALGORITHM.key,
    COMPLEXITY.key,
    TIME_COMPLEXITY.key,
    SPACE_COMPLEXITY.key,
    ASYMPTOTIC_BEHAVIOR.key,
    BOUND.key,
    UPPER_BOUND.key,
    BIG_O_NOTATION.key,
    GRAPH_LABELING.key,
    GRAPH_COLORING.key,
    VERTEX_COLORING.key,
    OVERLAPPING_SUBPROBLEMS.key,
    HASH_COLLISION.key,
    ROLLING_HASH.key,
    RABIN_KARP_ALGORITHM.key,
    BRUTE_FORCE.key,
    GREEDY_ALGORITHM.key,
    DYNAMIC_PROGRAMMING.key,
    DIVIDE_AND_CONQUER.key,
    RECURSION.key,
    BASE_CASE.key,
    REDUCTION.key,
    SORTING.key,
    SELECTION_SORT.key,
    QUICK_SORT.key,
    PROBABILITY.key,
    DISTRIBUTION.key,
    UNIFORM_DISTRIBUTION.key,
    MERGE.key,
    MERGE_SORT.key,
    BUCKET_SORT.key,
    RADIX_SORT.key,
    BUBBLE_SORT.key,
    TOPOLOGICAL_SORT.key,
    HEAP_SORT.key,
    BINARY_SEARCH.key,
    BOTTOM_UP_APPROACH.key,
    TOP_DOWN_APPROACH.key,
    HALF_AND_HALF_APPROACH.key,
)


class TrackDefinitionsAlgorithms(TrackDefinitionsAbstract):
    @staticmethod
    def get_track_definition_keys() -> tuple[DefinitionKey, ...]:
        """Get the track definition keys."""
        return _definition_keys
