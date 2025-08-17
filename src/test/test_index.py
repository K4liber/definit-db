from definit_db.data.field.index import get_index
from definit_db.definition.field import Field


def test_indexes_load_and_length():
    """By loading the index we check if there are no circular dependencies between definitions."""
    field_to_index_length = {Field.COMPUTER_SCIENCE: 39, Field.MATHEMATICS: 59}

    for field, index_length in field_to_index_length.items():
        field_index = get_index(field)
        assert len(field_index) == index_length
        assert all(definition_key.field == field for definition_key in field_index), (
            f"All definitions in the index for {field} should have the correct field."
        )
