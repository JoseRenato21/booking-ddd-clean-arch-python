class CEP:
    __slots__ =("_value",)

    def __init__(self, value: str) -> None:
        if not CEP._is_valid(value):
            raise ValueError("CEP inválido")
        self._value = value
    
    @property
    def value(self) -> str:
        return self._value
     
    def __eq__(self, other: object ) -> bool:
        return isinstance(other, CEP) and self._value == other._value
    
    def __hash__(self):
        return hash(self._value)
    
    def __repr__(self):
        return f"CEP(value='{self._value}')"
    
    @staticmethod
    def _is_valid(value: object) -> bool:
        if not isinstance(value, str):
            return False
        if len(value) != 8:
            return False
        if not value.isdigit():
            return False
        return True
    
    