from datetime import date

# Ajuste o import se o caminho/nome estiver diferente no seu projeto
from domain.shared.period import Period


def test_cria_periodo_valido():
    p = Period(date(2026, 2, 10), date(2026, 2, 12))
    assert p.start == date(2026, 2, 10)
    assert p.end == date(2026, 2, 12)


def test_nao_aceita_tipo_errado():
    try:
        Period("2026-02-10", "2026-02-12")  # type: ignore
        assert False, "Deveria ter levantado ValueError por tipo inválido"
    except ValueError:
        assert True


def test_nao_aceita_fim_igual_inicio():
    try:
        Period(date(2026, 2, 10), date(2026, 2, 10))
        assert False, "Deveria ter levantado ValueError quando fim == inicio"
    except ValueError:
        assert True


def test_nao_aceita_fim_antes_do_inicio():
    try:
        Period(date(2026, 2, 12), date(2026, 2, 10))
        assert False, "Deveria ter levantado ValueError quando fim < inicio"
    except ValueError:
        assert True


def test_qntd_noites():
    p = Period(date(2026, 2, 10), date(2026, 2, 15))
    assert p.qntd_noites() == 5


def test_eq_mesmo_valor():
    p1 = Period(date(2026, 2, 10), date(2026, 2, 12))
    p2 = Period(date(2026, 2, 10), date(2026, 2, 12))
    assert p1 == p2


def test_eq_valor_diferente():
    p1 = Period(date(2026, 2, 10), date(2026, 2, 12))
    p2 = Period(date(2026, 2, 10), date(2026, 2, 13))
    assert p1 != p2


def test_hash_igual_para_mesmo_valor():
    p1 = Period(date(2026, 2, 10), date(2026, 2, 12))
    p2 = Period(date(2026, 2, 10), date(2026, 2, 12))
    assert hash(p1) == hash(p2)


def test_set_remove_duplicado_por_hash_e_eq():
    p1 = Period(date(2026, 2, 10), date(2026, 2, 12))
    p2 = Period(date(2026, 2, 10), date(2026, 2, 12))
    s = {p1, p2}
    assert len(s) == 1


def test_repr_contem_infos():
    p = Period(date(2026, 2, 10), date(2026, 2, 12))
    r = repr(p)
    assert "Period" in r
    assert "inicio" in r
    assert "fim" in r