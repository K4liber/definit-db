from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.foundamental.call_stack import CALL_STACK
from definit_db.data.field.computer_science.definitions.foundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.foundamental.stack_memory import STACK_MEMORY
from definit_db.data.field.computer_science.definitions.foundamental.variable import VARIABLE
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION


class _StackOverflow(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} occurs when a {PROGRAM.key.get_reference()} attempts to use more {STACK_MEMORY.key.get_reference()} 
than is available. This typically happens when the {CALL_STACK.key.get_reference()} grows too large, often due to 
excessive {FUNCTION.key.get_reference()} {RECURSION.key.get_reference()} or allocating too many local {VARIABLE.key.get_reference("variables")}. When stack overflow occurs, 
the program usually terminates with an error.
"""


STACK_OVERFLOW = _StackOverflow(DefinitionKey(name="stack overflow", field=FieldName.COMPUTER_SCIENCE))
