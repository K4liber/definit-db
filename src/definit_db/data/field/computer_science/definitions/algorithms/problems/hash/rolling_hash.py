from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _RollingHash(Definition):
    def _get_content(self) -> str:
        return f"""
A rolling hash is an approach designed to enable efficient execution of the 
{HASH_FUNCTION.key.get_reference(phrase="hash function")} when the input is modified incrementally, such as when 
a window of fixed size moves over a {SEQUENCE.key.get_reference()}.
"""


ROLLING_HASH = _RollingHash(
    key=DefinitionKey(
        name="rolling_hash",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
