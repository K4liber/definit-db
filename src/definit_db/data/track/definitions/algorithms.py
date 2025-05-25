from definit_db.data.field.computer_science.definitions.algorithms.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.computer_science.definitions.algorithms.greedy_algorithm import GREEDY_ALGORITHM
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
from definit_db.data.field.computer_science.definitions.algorithms.problems.property.overlapping_subproblems import (
    OVERLAPPING_SUBPROBLEMS,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.rolling_hash import ROLLING_HASH
from definit_db.data.field.computer_science.definitions.algorithms.searching.string.rabin_karp_algorithm import (
    RABIN_KARP_ALGORITHM,
)
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.subproblem import SUBPROBLEM
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.optimal_substructure import OPTIMAL_SUBSTRUCTURE
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
    GRAPH_LABELING.key,
    GRAPH_COLORING.key,
    VERTEX_COLORING.key,
    OVERLAPPING_SUBPROBLEMS.key,
    HASH_COLLISION.key,
    ROLLING_HASH.key,
    RABIN_KARP_ALGORITHM.key,
    GREEDY_ALGORITHM.key,
    DIVIDE_AND_CONQUER.key,
    RECURSION.key,
    BASE_CASE.key,
    REDUCTION.key,
)


class TrackDefinitionsAlgorithms(TrackDefinitionsAbstract):
    @staticmethod
    def get_track_definition_keys() -> tuple[DefinitionKey, ...]:
        """Get the track definition keys."""
        return _definition_keys
