from datetime import date

class Period:
    
    __slots__ = ("_start","_end",)

    def __init__(self, start: date , end: date) -> None:
        if not isinstance(start, date) or not isinstance(end, date): # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("Datas passadas não são válidas")
        if end <= start:
            raise ValueError("Data inicial igual ou maior que final")
        self._start = start
        self._end = end
        
    @property
    def start(self) -> date:
        return self._start
    
    @property
    def end(self) -> date:
        return self._end

    def qntd_noites(self) -> int:
        return (self._end - self._start).days
    
    def __repr__(self) -> str:
        return f"Period(inicio={self._start}, fim={self._end})"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Period) and self._start == other._start and self._end == other._end
    
    def __hash__(self) -> int:
        return hash((self._start, self._end))