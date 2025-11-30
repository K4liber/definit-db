from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _LastInFirstOut(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an ordering principle where the most recently added element in a {SEQUENCE.key.get_reference()} 
is the first one to be removed. In this scheme, the last element that enters is the first one to exit, 
similar to a stack of plates where you can only access the top plate.
"""


LAST_IN_FIRST_OUT = _LastInFirstOut(DefinitionKey(name="last in first out", field=Field.MATHEMATICS))
