from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey
from definit.definition.field import Field

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science import computer_science_index
from definit_db.data.field.mathematics import mathematics_index

_field_to_index: dict[Field, dict[DefinitionKey, Definition]] = {
    FieldName.COMPUTER_SCIENCE: {definition.key: definition for definition in computer_science_index},
    FieldName.MATHEMATICS: {definition.key: definition for definition in mathematics_index},
}


def get_index(field: Field) -> dict[DefinitionKey, Definition]:
    return _field_to_index[field]
