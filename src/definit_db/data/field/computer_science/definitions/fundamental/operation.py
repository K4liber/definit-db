from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.object import OBJECT


class _Operation(Definition):
    def _get_content(self) -> str:
        return f"""
Operation is an action that is carried out to accomplish a given task. In the most simple scenario, it is an 
action performed on at least one {OBJECT.key.get_reference(phrase="object")}.
"""


OPERATION = _Operation(
    key=DefinitionKey(
        name="operation",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
