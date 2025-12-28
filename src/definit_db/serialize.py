import importlib
import os
from pathlib import Path

from definit.db.md import DatabaseMd
from definit.definition.definition import Definition
from definit.definition.definition import DefinitionKey
from definit.definition.field import Field

from definit_db.data.field import FieldName

_FIELDS = [FieldName.MATHEMATICS, FieldName.COMPUTER_SCIENCE]
_DEFINIT_DB_PACKAGE_ROOT = Path(os.path.dirname(__file__))
_PATH_DATA_MD = _DEFINIT_DB_PACKAGE_ROOT / "data_md"
_MODULE_FIELD = "definit_db.data.field"


def get_field_index(field: Field) -> list[Definition]:
    module = importlib.import_module(f"{_MODULE_FIELD}.{field}.index")
    return getattr(module, "field_index")


def serialize() -> Path:
    # Write Markdown files for each definition in the specified fields
    all_definitions: list[Definition] = []

    for field in _FIELDS:
        field_index = get_field_index(field=field)
        for definition in field_index:
            if not isinstance(definition, Definition):
                continue

            # Extract sub_categories from module path
            sub_categories = tuple(
                definition.__module__.removeprefix("src.")
                .removeprefix(_MODULE_FIELD)
                .removeprefix(f".{field}.definitions.")
                .split(".")
            )[:-1]  # Exclude the last part which is the definition module itself
            fixed_definition = Definition(
                key=DefinitionKey(name=definition.key.name, field=definition.key.field, sub_categories=sub_categories),
                content=definition.content,
            )
            all_definitions.append(fixed_definition)

    DatabaseMd.serialize(
        definitions=all_definitions,
        db_path=_PATH_DATA_MD,
    )
    return _PATH_DATA_MD


if __name__ == "__main__":
    serialize()
