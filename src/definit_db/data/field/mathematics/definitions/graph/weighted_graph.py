from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _WeightedGraph(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {GRAPH.key.get_reference()} in which each {EDGE.key.get_reference()} 
has an associated numerical value called a weight. The weight typically represents a cost, distance, 
capacity, or other metric relevant to the problem being modeled. Weighted graphs are used in many 
algorithms where the {RELATION.key.get_reference("relationship")} between nodes has varying significance or cost.
"""


WEIGHTED_GRAPH = _WeightedGraph(DefinitionKey(name="weighted graph", field=Field.MATHEMATICS))
