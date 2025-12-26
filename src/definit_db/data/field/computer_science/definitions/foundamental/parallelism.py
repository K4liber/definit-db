from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.concurrency import CONCURRENCY
from definit_db.data.field.computer_science.definitions.foundamental.core import CORE
from definit_db.data.field.computer_science.definitions.foundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.foundamental.processor import PROCESSOR
from definit_db.data.field.computer_science.definitions.foundamental.program import PROGRAM


class _Parallelism(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a form of {CONCURRENCY.key.get_reference()} where multiple {OPERATION.key.get_reference("operations")} 
or tasks are executed simultaneously at the exact same time, typically by utilizing multiple {PROCESSOR.key.get_reference("processors")} or {CORE.key.get_reference("cores")}. 
Unlike {CONCURRENCY.key.get_reference()}, which is about managing multiple tasks that may overlap in time, 
{self.key.get_reference()} specifically requires the physical simultaneous execution of tasks. This approach enables 
{PROGRAM.key.get_reference("programs")} to achieve significant performance improvements by dividing work across multiple processing units.
"""


PARALLELISM = _Parallelism(DefinitionKey(name="parallelism", field=FieldName.COMPUTER_SCIENCE))
