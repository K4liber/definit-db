from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _AdjacencyList(Definition):
    def _get_content(self) -> str:
        return f"""
An adjacency list is a way of representing a {GRAPH.key.get_reference(phrase="graph")} as a collection of lists. 
Each list corresponds to a {NODE.key.get_reference(phrase="node")} in the graph and contains a list of its 
adjacent nodes.
"""


ADJACENCY_LIST = _AdjacencyList(
    key=DefinitionKey(
        name="adjacency_list",
        field=FieldName.MATHEMATICS,
    )
)
