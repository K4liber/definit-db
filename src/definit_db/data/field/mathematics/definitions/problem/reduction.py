from definit_db.data.field.mathematics.definitions.foundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Reduction(Definition):
    def _get_content(self) -> str:
        return (
            f"Reduction refers to the rewriting of an expression into a simpler form."
            f"It is process of transforming a {PROBLEM.key.get_reference()} into a simpler or smaller instance of the "
            f"same or a {RELATION.key.get_reference('related')} problem, often to make it easier to solve."
        )


REDUCTION = _Reduction(
    key=DefinitionKey(
        name="reduction",
        field=Field.MATHEMATICS,
    )
)
