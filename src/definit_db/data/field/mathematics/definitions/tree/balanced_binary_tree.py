from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE


class _BalancedBinaryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {BINARY_TREE.key.get_reference(phrase="binary tree")} in which the depth of the two subtrees of every 
{NODE.key.get_reference(phrase="node")} never differs by more than one. This means that for any given node in the 
tree, the height of its left and right subtrees can differ by at most one.
"""


BALANCED_BINARY_TREE = _BalancedBinaryTree(
    key=DefinitionKey(
        name="balanced_binary_tree",
        field=FieldName.MATHEMATICS,
    )
)
