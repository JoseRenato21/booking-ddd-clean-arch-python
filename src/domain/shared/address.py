from __future__ import annotations

from src.domain.shared.cep import CEP


class Endereco:
    __slots__ = ("_rua", "_numero", "_cidade", "_estado", "_cep")

    def __init__(self, rua: str, numero: str, cidade: str, estado: str, cep: CEP) -> None:
        if not Endereco._is_valid(rua, numero, cidade, estado, cep):
            raise ValueError("Endereço inválido")

        # Aqui eu guardo normalizado “leve” (trim), sem inventar regras pesadas
        self._rua = rua.strip()
        self._numero = numero.strip()
        self._cidade = cidade.strip()
        self._estado = estado.strip().upper()
        self._cep = cep

    @property
    def rua(self) -> str:
        return self._rua

    @property
    def numero(self) -> str:
        return self._numero

    @property
    def cidade(self) -> str:
        return self._cidade

    @property
    def estado(self) -> str:
        return self._estado

    @property
    def cep(self) -> CEP:
        return self._cep

    def __repr__(self) -> str:
        return (
            "Endereco("
            f"rua='{self._rua}', "
            f"numero='{self._numero}', "
            f"cidade='{self._cidade}', "
            f"estado='{self._estado}', "
            f"cep={self._cep}"
            ")"
        )

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Endereco)
            and self._rua == other._rua
            and self._numero == other._numero
            and self._cidade == other._cidade
            and self._estado == other._estado
            and self._cep == other._cep
        )

    def __hash__(self) -> int:
        return hash((self._rua, self._numero, self._cidade, self._estado, self._cep))

    @staticmethod
    def _is_valid(rua: object, numero: object, cidade: object, estado: object, cep: object) -> bool:
        # Tipos
        if not isinstance(rua, str) or not isinstance(numero, str) or not isinstance(cidade, str) or not isinstance(estado, str):
            return False
        if not isinstance(cep, CEP):
            return False

        # Conteúdo mínimo (sem “normalização pesada”)
        if rua.strip() == "":
            return False
        if numero.strip() == "":
            return False
        if cidade.strip() == "":
            return False

        uf = estado.strip()
        if len(uf) != 2:
            return False
        if not uf.isalpha():
            return False

        return True