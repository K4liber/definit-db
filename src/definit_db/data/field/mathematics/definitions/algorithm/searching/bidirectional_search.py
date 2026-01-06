from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.searching.breadth_first_search import BREADTH_FIRST_SEARCH
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _BidirectionalSearch(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is an {ALGORITHM.key.get_reference()} for finding a {PATH.key.get_reference()} 
between two {NODE.key.get_reference("nodes")} in a {GRAPH.key.get_reference()}. It simultaneously searches 
forward from the start node and backward from the goal node, stopping when the two searches meet. This approach 
typically uses {BREADTH_FIRST_SEARCH.key.get_reference("breadth-first search")} from both directions. 
By searching from both ends, the algorithm can significantly reduce the search space and find the path more 
efficiently than searching in only one direction.
"""


BIDIRECTIONAL_SEARCH = _BidirectionalSearch(DefinitionKey(name="bidirectional search", field=FieldName.MATHEMATICS))
