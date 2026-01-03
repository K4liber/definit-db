from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.computation.turing_machine import TURING_MACHINE
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _NondeterministicTuringMachine(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {TURING_MACHINE.key.get_reference("Turing machine")} where each 
{INSTRUCTION.key.get_reference()} can have multiple possible next states and actions. Given the current 
state and the symbol being read, the machine can "choose" among several possible transitions, effectively 
exploring multiple computational paths simultaneously. This is a theoretical model that allows the machine 
to make the "right" choice at each step, making it more powerful than its deterministic counterpart for 
analyzing computational complexity.
"""


NONDETERMINISTIC_TURING_MACHINE = _NondeterministicTuringMachine(
    DefinitionKey(name="nondeterministic Turing machine", field=FieldName.MATHEMATICS)
)
