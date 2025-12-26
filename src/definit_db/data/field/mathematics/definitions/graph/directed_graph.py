from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _DirectedGraph(Definition):
    def _get_content(self) -> str:
        return f"""
A directed graph is a {GRAPH.key.get_reference(phrase="graph")} in which the 
{EDGE.key.get_reference(phrase="edges")} have a direction. Each edge connects an ordered pair of 
{NODE.key.get_reference(phrase="nodes")}, meaning that the connection goes from one node to another in a 
specific direction.
"""


DIRECTED_GRAPH = _DirectedGraph(
    key=DefinitionKey(
        name="directed_graph",
        field=FieldName.MATHEMATICS,
    )
)
