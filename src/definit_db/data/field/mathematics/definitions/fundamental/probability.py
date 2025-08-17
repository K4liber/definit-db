from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Probability(Definition):
    def _get_content(self) -> str:
        return (
            f"Probability is a measure that quantifies the likelihood "
            f"of elements in a {SET.key.get_reference('set')} or events, "
            f"typically expressed as a number between 0 and 1. Probabilities indicate how likely different "
            f"{OBJECT.key.get_reference(phrase='objects')} or outcomes are to occur."
        )


PROBABILITY = _Probability(
    key=DefinitionKey(
        name="probability",
        field=Field.MATHEMATICS,
    )
)
