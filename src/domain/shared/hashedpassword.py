class HashedPassword:
    
    __slots__ = ("_value",)

    def __init__(self, value: str) -> None:
        if not self._is_valid(value):
            raise ValueError("Hash inválido")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return "HashedPassword(value='***')"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, HashedPassword) and self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

    @staticmethod
    def _is_valid(value: object) -> bool:
        if not isinstance(value, str):
            return False
        if len(value) < 20:  # hash normalmente é longo
            return False
        return True