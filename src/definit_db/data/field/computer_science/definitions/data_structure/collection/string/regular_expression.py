from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.mathematics.definitions.fundamental.notations.label import LABEL
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _RegularExpression(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {SEQUENCE.key.get_reference()} of 
{CHARACTER_ENCODING.key.get_reference("characters")} that defines a search pattern for 
{STRING.key.get_reference("strings")}. Regular expressions use special syntax to specify patterns, including 
literal {CHARACTER_ENCODING.key.get_reference("characters")}, character classes, quantifiers, and anchors. They 
enable powerful text matching, searching, and manipulation operations, allowing users to find, extract, or replace text 
that matches specific patterns. For example, the pattern `[0-9]+` matches one or more digits, and `^[a-z]+$` matches 
{STRING.key.get_reference("strings")} containing only lowercase letters from start to end. Regular expressions 
can also use groups and {LABEL.key.get_reference("labels")} to capture and reference parts of the matched text.
"""


REGULAR_EXPRESSION = _RegularExpression(DefinitionKey(name="regular expression", field=Field.COMPUTER_SCIENCE))
