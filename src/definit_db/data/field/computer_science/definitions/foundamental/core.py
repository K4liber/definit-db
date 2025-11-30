from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.processor import PROCESSOR
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Core(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an independent processing unit within a {PROCESSOR.key.get_reference()} 
that can execute {INSTRUCTION.key.get_reference("instructions")} and perform {OPERATION.key.get_reference("operations")} 
independently of other cores. Modern processors often contain multiple cores, enabling them to execute multiple 
tasks simultaneously, which is essential for parallel computing.
"""


CORE = _Core(DefinitionKey(name="core", field=Field.COMPUTER_SCIENCE))
