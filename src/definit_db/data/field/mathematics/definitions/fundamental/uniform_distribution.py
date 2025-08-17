from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _UniformDistribution(Definition):
    def _get_content(self) -> str:
        return (
            f"A uniform distribution is a {DISTRIBUTION.key.get_reference()} in which all elements of a "
            f"{SET.key.get_reference('set')} are assigned equal weight or probability, "
            f"so each outcome is equally likely."
        )


UNIFORM_DISTRIBUTION = _UniformDistribution(
    key=DefinitionKey(
        name="uniform_distribution",
        field=Field.MATHEMATICS,
    )
)
