from datetime import date

class Periodo:
    
    __slots__ = ("_i_date","e_date","_value_date", "_period",)

def __init__(self, value_date : int, i_date: date , e_date: date , period: enumerate) -> None:
    self._value_date = value_date

@property
def value_date(self) -> int:
    return self._value_date
