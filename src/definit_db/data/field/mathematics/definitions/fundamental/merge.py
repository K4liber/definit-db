from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Merge(Definition):
    def _get_content(self) -> str:
        return f"""
Merge is an {OPERATION.key.get_reference()} that combines two {SEQUENCE.key.get_reference("sequences")} into a 
single sequence by interleaving their elements while preserving the order of each input sequence.
"""


MERGE = _Merge(
    key=DefinitionKey(
        name="merge",
        field=FieldName.MATHEMATICS,
    )
)
