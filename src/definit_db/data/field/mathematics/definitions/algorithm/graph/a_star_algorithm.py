from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.greedy_algorithm import GREEDY_ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.heuristic import HEURISTIC
from definit_db.data.field.mathematics.definitions.algorithm.graph.dijkstras_algorithm import DIJKSTRAS_ALGORITHM
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _AStarAlgorithm(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        dijkstra_ref = DIJKSTRAS_ALGORITHM.key.get_reference("Dijkstra's algorithm")
        return f"""
The {self.key.get_reference()} is a {GREEDY_ALGORITHM.key.get_reference("greedy")} 
{ALGORITHM.key.get_reference()} that finds the shortest {PATH.key.get_reference()} between two 
{NODE.key.get_reference("nodes")} in a weighted {GRAPH.key.get_reference()}. It extends 
{dijkstra_ref} by using a {HEURISTIC.key.get_reference("heuristic function")} 
to estimate the {GRAPH_DISTANCE.key.get_reference("distance")} from the current node to the goal node, 
allowing it to prioritize more promising paths and find the shortest path more efficiently. 
The algorithm maintains two costs: the actual cost from the start node (g-score) and the estimated 
total cost through the current node to the goal (f-score = g-score + heuristic). 
It requires the heuristic to be admissible (never overestimating the actual cost) to guarantee 
finding the optimal path.
"""


A_STAR_ALGORITHM = _AStarAlgorithm(DefinitionKey(name="A-star algorithm", field=FieldName.MATHEMATICS))
