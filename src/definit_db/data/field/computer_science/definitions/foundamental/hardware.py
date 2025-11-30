from definit_db.data.field.computer_science.definitions.foundamental.computer import COMPUTER
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Hardware(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} refers to the physical components of a {COMPUTER.key.get_reference()} system. 
These are tangible parts that can be touched and manipulated.
"""


HARDWARE = _Hardware(DefinitionKey(name="hardware", field=Field.COMPUTER_SCIENCE))
