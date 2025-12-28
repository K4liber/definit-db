from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.problem.algorithm.time_complexity import TIME_COMPLEXITY


class _FloydWarshallAlgorithm(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is an {ALGORITHM.key.get_reference()} that finds the shortest 
{PATH.key.get_reference("paths")} between all pairs of {NODE.key.get_reference("nodes")} in a weighted 
{GRAPH.key.get_reference()}. The algorithm uses {DYNAMIC_PROGRAMMING.key.get_reference("dynamic programming")} 
by iteratively considering each node as an intermediate node and updating the 
{GRAPH_DISTANCE.key.get_reference("distances")} between all pairs of nodes if a shorter path through 
the intermediate node is found. It can handle negative {EDGE.key.get_reference("edge")} weights but 
cannot handle negative-weight {CYCLE.key.get_reference("cycles")}. The algorithm has a {TIME_COMPLEXITY.key.get_reference("time complexity")} 
of O(V³) where V is the number of nodes, making it efficient for dense graphs or when all-pairs shortest paths are needed.
"""


FLOYD_WARSHALL_ALGORITHM = _FloydWarshallAlgorithm(
    DefinitionKey(name="Floyd-Warshall algorithm", field=FieldName.MATHEMATICS)
)
