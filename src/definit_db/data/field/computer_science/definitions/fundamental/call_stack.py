from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.stack_memory import STACK_MEMORY
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _CallStack(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a region of {STACK_MEMORY.key.get_reference()} that tracks active 
{FUNCTION.key.get_reference("function")} calls during {PROGRAM.key.get_reference()} execution. 
It stores {INFORMATION.key.get_reference()} about each function call, including where to return after 
the function completes. When a function is called, its information is added to the call stack, 
and when it returns, that information is removed.
"""


CALL_STACK = _CallStack(DefinitionKey(name="call stack", field=FieldName.COMPUTER_SCIENCE))
