from definit_db.data.field.index import get_index
from definit_db.definition.definition import Definition
from definit_db.definition.field import Field
from src.test.utils import get_all_definitions

_field_to_index_length = {Field.COMPUTER_SCIENCE: 38, Field.MATHEMATICS: 70}


def test_indexes_load_and_length():
    """By loading the index we check if there are no circular dependencies between definitions."""
    for field, index_length in _field_to_index_length.items():
        field_index = get_index(field)
        assert len(field_index) == index_length
        assert all(definition_key.field == field for definition_key in field_index), (
            f"All definitions in the index for {field} should have the correct field."
        )


def test_all_definitions_in_indexes():
    all_definitions_in_indexes: set[Definition] = set()

    for field in _field_to_index_length.keys():
        field_index = get_index(field)
        all_definitions_in_indexes.update({definition for definition in field_index.values()})

    all_definitions = get_all_definitions()
    definitions_diff = all_definitions - all_definitions_in_indexes
    assert not definitions_diff, (
        f"The following definitions are missing in the indexes: "
        f"{', '.join(definition.key.name for definition in definitions_diff)}"
    )
