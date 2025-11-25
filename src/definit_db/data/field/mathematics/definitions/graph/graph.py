from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Graph(Definition):
    def _get_content(self) -> str:
        return f"""
Graphs are used to model pairwise {RELATION.key.get_reference(phrase="relations")} between objects. 
A graph is made up of {NODE.key.get_reference(phrase="nodes")} and {EDGE.key.get_reference(phrase="edges")}. 
Graphs can be directed or undirected, weighted or unweighted, and can represent various types of 
relationships in different fields.
"""


GRAPH = _Graph(
    key=DefinitionKey(
        name="graph",
        field=Field.MATHEMATICS,
    )
)
