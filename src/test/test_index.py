from definit_db.data.field.index import get_index
from definit_db.definition.field import Field


def test_indexes_load_and_length():
    """By loading the index we check if there are no circular dependencies between definitions."""
    field_to_index_length = {Field.COMPUTER_SCIENCE: 40, Field.MATHEMATICS: 44}

    for field, index_length in field_to_index_length.items():
        field_index = get_index(field)
        assert len(field_index) == index_length
