from definit_db.data.field.mathematics.definitions.problem.algorithm.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.algorithm.optimization import OPTIMIZATION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Bud(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an {OPTIMIZATION.key.get_reference()} framework for improving {ALGORITHM.key.get_reference("algorithms")} 
by identifying and addressing three types of inefficiencies: Bottlenecks (the slowest parts that limit overall performance), 
Unnecessary work (operations that can be eliminated without affecting the result), and Duplicated work (redundant computations 
that can be avoided by reusing previously computed results). By systematically examining these three areas, BUD helps 
identify opportunities for performance improvement.
"""


BUD = _Bud(DefinitionKey(name="BUD", field=Field.MATHEMATICS))
