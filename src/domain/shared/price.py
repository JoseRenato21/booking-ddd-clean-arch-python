from decimal import Decimal, InvalidOperation

class Price:

    __slots__ = ("_value",)
    
    def __init__(self, value: str | int | Decimal) -> None:
        if not Price._is_valid(value):
            raise  ValueError("Price inválido")
        self._value = Price._normalize(value)
    
    def somar(self, outro: object) -> "Price":
        if not isinstance(outro, Price): #o pynance ta confiando na linguagem.   
            raise TypeError("Só é possível somar Price com Price")
        return Price(self._value + outro._value)
    
    def subtrair(self, outro: object) -> "Price":
        if not isinstance(outro, Price): # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("só é possível subtrair com Price")
        res = self.value - outro._value
        if res < Decimal("0.00"):
            raise ValueError("valor não pode ser negativo")
        return Price(res)
    
    def multiplicar(self, outro: Decimal | int) -> "Price":
        if not isinstance(outro, (Decimal, int)): # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("o multiplicador precisa ser decimal ou inteiro")
        fator = Decimal(str(outro))
        if fator < 0:
            raise ValueError("multiplicador não pode ser negativo")
        return Price(self._value * fator)

    @property
    def value(self) -> Decimal:
        return self._value
    
    def __repr__(self) -> str:
        return f"Price(value='{self._value}')"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Price) and self._value == other._value
    
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
            d = Price._normalize(value)
            return d >= Decimal("0.00")
        except (ValueError, InvalidOperation, TypeError):
            return False