class Password:
    
    __slots__ = ("_value",)

    def __init__(self, value: str) -> None:
        if not Password._is_valid(value):
            raise ValueError("Senha inválida")
        self._value = value
    
    @property
    def value(self) -> str: 
        return self._value
    
    def __repr__(self) -> str:
        return f"Password(value='{self._value}')"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Password) and self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    @staticmethod
    def _is_valid(value: object) -> bool:
        if not isinstance(value, str):
            return False
        if len(value) < 8:
            return False
        if value.isdigit() or value.isalpha():
            return False
        return True