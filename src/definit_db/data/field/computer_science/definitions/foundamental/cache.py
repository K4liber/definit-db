from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.data import DATA


class _Cache(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a high-speed {COMPUTER_MEMORY.key.get_reference()} storage layer that temporarily 
holds frequently accessed or recently used {DATA.key.get_reference()} to reduce access time and improve performance. 
When data is requested, the cache is checked first; if the data is found (a cache hit), it can be retrieved quickly 
without accessing slower storage. If not found (a cache miss), the data must be fetched from the original source 
and may be stored in the cache for future use.
"""


CACHE = _Cache(DefinitionKey(name="cache", field=FieldName.COMPUTER_SCIENCE))
