from definit_db.data.field.computer_science.definitions.data_structure.map import MAP
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _CharacterEncoding(Definition):
    def _get_content(self) -> str:
        return f"""
A method of representing characters as numerical values, allowing computers to store and manipulate text. 
Character encoding schemes define the {MAP.key.get_reference(phrase="mapping")} between characters and their 
corresponding numerical values.
"""


CHARACTER_ENCODING = _CharacterEncoding(
    key=DefinitionKey(
        name="character_encoding",
        field=Field.COMPUTER_SCIENCE,
    )
)
