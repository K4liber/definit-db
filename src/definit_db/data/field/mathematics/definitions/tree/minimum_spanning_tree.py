from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _MinimumSpanningTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {TREE.key.get_reference(phrase="tree")} that connects all the {NODE.key.get_reference(phrase="nodes")} in a 
{GRAPH.key.get_reference(phrase="graph")} with the minimum possible total {EDGE.key.get_reference(phrase="edge")} 
weight. In other words, it is a subset of the edges of the graph that forms a tree and includes every node, such 
that the sum of the weights of the edges is minimized.
"""


MINIMUM_SPANNING_TREE = _MinimumSpanningTree(
    key=DefinitionKey(
        name="minimum_spanning_tree",
        field=FieldName.MATHEMATICS,
    )
)
