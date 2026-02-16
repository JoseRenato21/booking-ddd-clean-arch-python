class Phone:
    
    __slots__ = ("_value",)
    
    def __init__(self, value: str) -> None:
        if not Phone._is_valid(value):
            raise ValueError("Número digitado incorretamente")
        self._value = value
        
    @property
    def value(self) -> str:
        return self._value
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Phone) and self._value == other._value
    
    def __hash__(self):
        return hash(self._value)
    
    def __repr__(self):
        return f"Phone(value='{self._value}')"
    
    def ddd(self):
        return self._value[0:2]
        
    @staticmethod
    def _is_valid(value: object):
        if not isinstance(value, str):
            return False
        if len(value) != 11:
            return False
        if not value.isdigit():
            return False
        return True
        