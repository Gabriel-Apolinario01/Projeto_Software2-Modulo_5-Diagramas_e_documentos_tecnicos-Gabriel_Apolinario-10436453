# Projeto Software - Módulo 5
## Diagramas e Documentos Técnicos

---

## Descrição
Este módulo faz parte de uma plataforma de documentação inteligente baseada em microsserviços e Inteligência Artificial.

O Módulo 5 é responsável por gerar automaticamente diagramas e documentação técnica a partir de código-fonte.

---

## Objetivo
Gerar diagramas UML e auxiliar na documentação técnica de projetos de software de forma automatizada.

---

## Funcionalidades
- Geração de diagramas UML a partir de código
- Simulação de engenharia reversa
- Estrutura base para documentação automática
- API para integração com outros módulos

---

## Arquitetura do Módulo
O módulo funciona como um microsserviço independente.

Fluxo:

Usuário → Frontend → Microsserviço → Parser → Gerador UML → Resposta

---

## Como executar o projeto

## 1. Instalar dependências

pip install -r requirements.txt

## 2. Executar o servidor
python -m uvicorn main:app --reload

## 3. Acessar a API

Abra no navegador:
http://127.0.0.1:8000/docs

Endpoint principal
POST /generate-diagram

Entrada:
{
  "code": "class User {}"
}

Saída:
{
  "diagram": "@startuml ...",
  "message": "Diagrama gerado com sucesso"
}

Testes
A API pode ser testada diretamente pela interface interativa disponibilizada em /docs.

---

Tecnologias utilizadas
Python
FastAPI
Uvicorn

---

Integrantes
Gabriel Apolinário
Leonardo Zani
Felipe Yuji