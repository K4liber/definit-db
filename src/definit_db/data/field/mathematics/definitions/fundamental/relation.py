from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Relation(Definition):
    def _get_content(self) -> str:
        return (
            "A relation (also called relationship) describes a connection or association between elements of a "
            f"{SET.key.get_reference(phrase='set(s)')}."
        )


RELATION = _Relation(
    key=DefinitionKey(
        name="relation",
        field=Field.MATHEMATICS,
    )
)
