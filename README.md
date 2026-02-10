# Booking Domain – DDD & Clean Architecture (Python)

Este projeto é um **sistema de Booking** desenvolvido em **Python**, com foco em **Domain-Driven Design (DDD)**, **Clean Architecture** e **Programação Orientada a Objetos (POO)**.

O objetivo principal é **modelar o domínio corretamente**, priorizando:
- regras de negócio explícitas
- isolamento do domínio
- código testável e evolutivo
- independência de frameworks

> Este projeto está sendo desenvolvido de forma incremental, com commits pequenos e focados, simulando um ambiente profissional.

---

## 🎯 Objetivos do Projeto

- Praticar **DDD aplicado de verdade** (não apenas teoria)
- Estruturar um projeto seguindo **Clean Architecture**
- Criar **Value Objects ricos**, com invariantes bem definidas
- Separar claramente **Domínio**, **Aplicação** e **Infraestrutura**
- Servir como **projeto de portfólio** e base para estudos avançados

---

## 🧠 Conceitos Aplicados

### Domain-Driven Design (DDD)
- Value Objects imutáveis
- Entidades com identidade
- Agregados bem definidos
- Regras de negócio protegidas no domínio
- Linguagem ubíqua

### Clean Architecture
- Dependências sempre apontam **para dentro**
- Domínio independente de frameworks
- Camadas bem definidas
- Infraestrutura como detalhe

---

## 🗂️ Estrutura do Projeto

```text
src/
├── domain/
│   ├── shared/            # Value Objects (Shared Kernel)
│   ├── hospede.py         # Entidades de domínio
│   ├── quarto.py
|   └── ...
│
├── application/           # Casos de uso (em construção)
├── infrastructure/        # Infra (DB, APIs, etc.)
└── tests/                 # Testes automatizados
