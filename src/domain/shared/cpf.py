class CPF:

    __slots__ = ("_value",)
    
    def __init__(self, value: str) -> None:
        if not CPF._is_valid(value):
            raise ValueError("CPF inválido")
        self._value = value
    
    @property
    def value(self) -> str:
        return self._value
    
    def format_cpf(self) -> str:
        return f'{self._value[0:3]}.{self._value[3:6]}.{self._value[6:9]}-{self._value[9:11]}'
    
    
    def __repr__(self) -> str:
        return f"CPF(value='{self._value}')"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, CPF) and self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    @staticmethod
    def _is_valid(value: object ) -> bool: #aqui uso value pois e diferente
        if not isinstance(value, str):
            return False
        if len(value) != 11:
            return False
        if not value.isdigit():
            return False
        return True
    