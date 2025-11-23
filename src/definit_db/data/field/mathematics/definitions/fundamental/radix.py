from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Radix(Definition):
    def _get_content(self) -> str:
        return (
            "A radix is the base of a positional number system. "
            "It is the number of unique digits, including the digit zero, used to represent numbers. "
            "For example, base-10 (decimal) has radix 10. "
        )


RADIX = _Radix(
    key=DefinitionKey(
        name="radix",
        field=Field.MATHEMATICS,
    )
)
