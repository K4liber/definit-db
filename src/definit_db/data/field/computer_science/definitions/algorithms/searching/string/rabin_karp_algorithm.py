from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.algorithms.problems.hash.rolling_hash import ROLLING_HASH
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.substring import SUBSTRING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION


class _RabinKarpAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A string searching {ALGORITHM.key.get_reference()} that uses a 
{ROLLING_HASH.key.get_reference(phrase="rolling hash")} to find a pattern in a {STRING.key.get_reference()}. 
It computes the {HASH_FUNCTION.key.get_reference(phrase="hash")} of the pattern and the hash of each 
{SUBSTRING.key.get_reference()} of the text of the same length as the pattern, and compares them to find matches.
"""


RABIN_KARP_ALGORITHM = _RabinKarpAlgorithm(
    key=DefinitionKey(
        name="rabin_karp_algorithm",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
