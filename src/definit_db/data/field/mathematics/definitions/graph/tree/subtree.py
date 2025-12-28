from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.tree.tree import TREE


class _Subtree(Definition):
    def _get_content(self) -> str:
        return f"""
A {TREE.key.get_reference(phrase="tree")} formed from a {NODE.key.get_reference(phrase="node")} and all its 
descendants in a tree.
"""


SUBTREE = _Subtree(
    key=DefinitionKey(
        name="subtree",
        field=FieldName.MATHEMATICS,
    )
)
