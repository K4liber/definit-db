from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.greedy_algorithm import GREEDY_ALGORITHM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _DijkstrasAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A {GREEDY_ALGORITHM.key.get_reference(phrase="greedy")} {ALGORITHM.key.get_reference()} that finds the shortest 
{PATH.key.get_reference("paths")} from a single source {NODE.key.get_reference()} to all other 
nodes in a weighted {GRAPH.key.get_reference()} with non-negative 
{EDGE.key.get_reference("edge")} weights. The algorithm maintains a set of nodes for which the shortest 
{GRAPH_DISTANCE.key.get_reference("distance")} from the source is known, and iteratively selects the node with 
the minimum distance to expand the set until all nodes are processed.
"""


DIJKSTRAS_ALGORITHM = _DijkstrasAlgorithm(
    key=DefinitionKey(
        name="dijkstras_algorithm",
        field=Field.MATHEMATICS,
    )
)
