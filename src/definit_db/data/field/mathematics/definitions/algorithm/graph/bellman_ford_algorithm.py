from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.graph.dijkstras_algorithm import DIJKSTRAS_ALGORITHM
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _BellmanFordAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} that computes shortest {PATH.key.get_reference("paths")} from a single source 
{NODE.key.get_reference()} to all other nodes in a weighted {GRAPH.key.get_reference()}. The algorithm iteratively 
relaxes all {EDGE.key.get_reference("edges")} by updating {GRAPH_DISTANCE.key.get_reference("distances")} if a 
shorter path is found, repeating this process for each node in the graph. Unlike 
{DIJKSTRAS_ALGORITHM.key.get_reference("Dijkstra's algorithm")}, Bellman-Ford can handle negative edge weights and 
can detect negative-weight {CYCLE.key.get_reference("cycles")}, making it more versatile for certain applications.
"""


BELLMAN_FORD_ALGORITHM = _BellmanFordAlgorithm(
    key=DefinitionKey(
        name="bellman_ford_algorithm",
        field=FieldName.MATHEMATICS,
    )
)
