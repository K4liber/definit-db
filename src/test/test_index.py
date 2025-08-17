import importlib
import pkgutil
from collections import deque

import definit_db
from definit_db.data.field.index import get_index
from definit_db.definition.definition import Definition
from definit_db.definition.field import Field

_field_to_index_length = {Field.COMPUTER_SCIENCE: 39, Field.MATHEMATICS: 62}


def test_indexes_load_and_length():
    """By loading the index we check if there are no circular dependencies between definitions."""
    for field, index_length in _field_to_index_length.items():
        field_index = get_index(field)
        assert len(field_index) == index_length
        assert all(definition_key.field == field for definition_key in field_index), (
            f"All definitions in the index for {field} should have the correct field."
        )


def test_all_definitions_in_indexes():
    all_definitions_in_indexes: set[type[Definition]] = set()

    for field in _field_to_index_length.keys():
        field_index = get_index(field)
        all_definitions_in_indexes.update({type(definition) for definition in field_index.values()})

    # check how many classes inherits from Definition
    for _, name, _ in pkgutil.walk_packages(definit_db.__path__, definit_db.__name__ + "."):
        importlib.import_module(name)

    # Collect subclasses recursively
    all_definitions: set[type[Definition]] = set()
    q = deque([Definition])

    while q:
        cls = q.popleft()
        for sub in cls.__subclasses__():
            if sub not in all_definitions:
                all_definitions.add(sub)
                q.append(sub)

    assert len(all_definitions_in_indexes) == len(all_definitions)
