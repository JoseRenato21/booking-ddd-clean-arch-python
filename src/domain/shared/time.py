from datetime import time as _time


class Time:
    __slots__ = ("_value",)

    def __init__(self, value: _time) -> None:
        if not isinstance(value, _time): # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError("Horário inválido")
        normalized = value.replace(second=0, microsecond=0)
        self._value = normalized

    @property
    def value(self) -> _time:
        return self._value

    def __repr__(self) -> str:
        # Exibe apenas HH:MM
        return f"Time({self._value.strftime('%H:%M')})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Time) and self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)