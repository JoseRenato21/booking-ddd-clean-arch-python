from src.domain.shared.cpf import CPF
from src.domain.shared.email import Email


def test_email_basico() -> None:
    e = Email("Jose@GMAIL.com")
    assert e.value == "Jose@gmail.com"  # domínio normalizado
    assert repr(e) == "Email(value='Jose@gmail.com')"


def test_cpf_basico() -> None:
    cpf = CPF("12345678900")
    assert cpf.value == "12345678900"
    assert cpf.format_cpf() == "123.456.789-00"
    assert repr(cpf) == "CPF(value='12345678900')"


def test_cpf_invalido() -> None:
    try:
        CPF("123")
        assert False, "Era para ter levantado ValueError"
    except ValueError:
        pass


def test_igualdade_e_hash() -> None:
    a = CPF("12345678900")
    b = CPF("12345678900")
    c = CPF("00000000000")

    assert a == b
    assert a != c
    assert len({a, b}) == 1


if __name__ == "__main__":
    # roda “na mão” sem pytest
    test_email_basico()
    test_cpf_basico()
    test_cpf_invalido()
    test_igualdade_e_hash()
    print("✅ todos os testes passaram")