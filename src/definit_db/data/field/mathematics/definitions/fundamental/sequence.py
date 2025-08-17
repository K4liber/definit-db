from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Sequence(Definition):
    def _get_content(self) -> str:
        return (
            f"A collection of {OBJECT.key.get_reference(phrase='objects')} "
            f"in which repetitions are allowed and order matters."
        )


SEQUENCE = _Sequence(
    key=DefinitionKey(
        name="sequence",
        field=Field.MATHEMATICS,
    )
)
