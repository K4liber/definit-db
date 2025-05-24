from definit_db.data.field.computer_science.definitions.foundamental.data import DATA
from definit_db.data.field.mathematics.definitions.foundamental.set import SET
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _DataType(Definition):
    def _get_content(self) -> str:
        return (
            f"Data type (or simply type) is a grouping of {DATA.key.get_reference(phrase='data')} values, usually specified by a "
            f"{SET.key.get_reference(phrase='set')} of possible values, a {SET.key.get_reference(phrase='set')} of allowed operations on these values, "
            "and/or a representation of these values as machine types."
        )


DATA_TYPE = _DataType(
    key=DefinitionKey(
        name="data_type",
        field=Field.COMPUTER_SCIENCE,
    )
)
