from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Bit(Definition):
    def _get_content(self) -> str:
        return f"""
The bit (binary digit) is the smallest unit of data in computing, representing a binary state of either 0 or 1. 
Bits are the fundamental building blocks of {DATA.key.get_reference(phrase="data")} and can convey basic forms of 
{INFORMATION.key.get_reference(phrase="information")} by representing true/false or data/off states.
"""


BIT = _Bit(
    key=DefinitionKey(
        name="bit",
        field=Field.COMPUTER_SCIENCE,
    )
)
