from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Polynomial(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a mathematical expression consisting of variables and coefficients, 
involving only the {OPERATION.key.get_reference("operations")} of addition, subtraction, multiplication, 
and non-negative {INTEGER.key.get_reference("integer")} exponentiation of variables. A 
{self.key.get_reference()} is a type of {FUNCTION.key.get_reference()} that can be written in the form 
a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0, where the coefficients a_i are constants and n is a 
non-negative {INTEGER.key.get_reference("integer")} called the degree of the polynomial.
"""


POLYNOMIAL = _Polynomial(DefinitionKey(name="polynomial", field=FieldName.MATHEMATICS))
