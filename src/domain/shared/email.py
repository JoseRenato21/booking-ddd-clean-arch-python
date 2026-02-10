class Email:
    __slots__ = ("_value",)
    # __slots__ define quais atributos essa classe pode ter.
    # Aqui estamos dizendo: só pode existir o atributo _value.
    # Isso impede criar atributos por engano (ex: self.valeu, self.email, etc).

    def __init__(self, value: str):
        if not Email._is_valid(value):
            raise ValueError("Email inválido")

        # strip() remove espaços no começo e no fim da string.
        # Ex: " email@teste.com " -> "email@teste.com"
        # Isso evita rejeitar emails válidos por erro de digitação comum.
        value = value.strip()

        local, _, domain = value.partition('@')

        # Normalização do domínio:
        # Domínios de email NÃO são case-sensitive.
        # Ou seja: gmail.com == GMAIL.COM == Gmail.Com
        # Ao salvar sempre em lowercase, garantimos:
        # - comparações corretas
        # - igualdade por valor (DDD)
        self._value = f"{local}@{domain.lower()}"

    @property
    def value(self):
        # @property transforma este método em um "atributo de leitura".
        # Quem usa a classe escreve: email.value
        # Mas por baixo dos panos, isso chama esta função.
        # Como NÃO existe setter, esse valor NÃO pode ser alterado.
        return self._value

    def __eq__(self, other: object) -> bool:
        # Dois Emails são iguais se:
        # - são da mesma classe
        # - possuem exatamente o mesmo valor interno
        # Isso reforça o conceito de Value Object (igualdade por valor).
        return isinstance(other, Email) and self._value == other._value

    def __hash__(self):
        # Permite que Email seja usado em:
        # - sets
        # - chaves de dicionário
        # Como o objeto é imutável, o hash é seguro.
        return hash(self._value)

    def __repr__(self):
        # __repr__ define como o objeto aparece em:
        # - prints
        # - logs
        # - debugging
        # Isso NÃO é apenas estética: ajuda muito a entender
        # o estado do domínio durante testes e erros.
        return f"Email(value='{self._value}')"

    @staticmethod
    def _is_valid(value: object) -> bool:
        # Validação básica de tipo
        if not isinstance(value, str):
            return False

        # Remove espaços para evitar falsos negativos
        value = value.strip()

        # Email não pode conter espaços internos
        if " " in value:
            return False

        # Deve conter exatamente um '@'
        if value.count('@') != 1:
            return False

        local, _, domain = value.partition('@')

        # Validação da parte local (antes do @)
        if not local:
            return False
        if local.startswith('.') or local.endswith('.'):
            return False

        # '..' não é permitido nem no local nem no domínio
        if '..' in value:
            return False

        # Validação do domínio (depois do @)
        if not domain:
            return False
        if "." not in domain:
            return False
        if domain.startswith('.') or domain.endswith('.'):
            return False

        # Extração do TLD (última parte do domínio)
        # Ex: empresa.com.br -> br
        *_, tld = domain.split('.')

        # TLD deve ter pelo menos 2 letras (ex: com, br, net)
        if len(tld) < 2:
            return False

        # TLD deve conter apenas letras (sem números)
        if not tld.isalpha():
            return False

        return True