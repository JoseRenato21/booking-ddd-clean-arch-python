from decimal import Decimal, InvalidOperation

class Preco:

    __slots__ = ("_value",)
    
    def __init__(self, value: str | int | Decimal) -> None:
        if not Preco._is_valid(value):
            raise  ValueError("Preco inválido")
        self._value = Preco._normalize(value)
    
    def somar(self, outro: "Preco") -> "Preco":
        if not isinstance(outro, Preco): #o pynance ta confiando na linguagem
            raise TypeError("Só é possível somar preco com preco")
        return Preco(self._value + outro._value)
    
    def subtrair(self, outro: "Preco") -> "Preco":
        if not isinstance(outro, Preco):
            raise TypeError("só é possível subtrair com preco")
        res = self.value - outro._value
        if res < Decimal("0.00"):
            raise ValueError("valor não pode ser negativo")
        return Preco(res)
    
    def multiplicar(self, outro: Decimal | int) -> "Preco":
        if not isinstance(outro, (Decimal, int)):
            raise TypeError("o multiplicador precisa ser decimal ou inteiro")
        fator = Decimal(str(outro))
        if fator < 0:
            raise ValueError("multiplicador não pode ser negativo")
        return Preco(self._value * fator)

    @property
    def value(self) -> Decimal:
        return self._value
    
    def __repr__(self) -> str:
        return f"Preco(value='{self._value}')"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Preco) and self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    @staticmethod
    def _normalize(value: str | int | Decimal) -> Decimal:
        value_str = str(value).strip()
        if value_str == "":
            raise ValueError
        decimal_value = Decimal(value_str)
        return  decimal_value.quantize(Decimal('0.00'))
    
    @staticmethod
    def _is_valid(value: object ) -> bool: #aqui uso value pois e diferente
        if not isinstance(value, (int, str, Decimal)):
            return False
        try:
            d = Preco._normalize(value)
            return d >= Decimal("0.00")
        except (ValueError, InvalidOperation, TypeError):
            return False