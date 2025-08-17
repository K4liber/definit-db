from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Distribution(Definition):
    def _get_content(self) -> str:
        return (
            "A distribution describes how values (or outcomes) are spread over a domain. "
            f"Typically it associates elements of a {SET.key.get_reference('set')} "
            f"or values to their frequencies or {PROBABILITY.key.get_reference(phrase='probabilities')}, "
            f"describing how likely or how common different {OBJECT.key.get_reference(phrase='objects')} are."
        )


DISTRIBUTION = _Distribution(
    key=DefinitionKey(
        name="distribution",
        field=Field.MATHEMATICS,
    )
)
