# 📚 Sistema de Gerenciamento de Biblioteca

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de consolidar a base em Python, aplicando na prática conceitos fundamentais como:

- Programação orientada a objetos (POO)
- Manipulação de arquivos (leitura e escrita em JSON)
- Estruturas de dados (dicionários)
- Modularização do código
- Tratamento de exceções

Além disso, o projeto simula um sistema real de gerenciamento, permitindo compreender na prática como funciona a persistência de dados e a organização de aplicações em camadas.

## 🚀 Funcionalidades

- ✅ Cadastrar livros
- ✅ Listar livros cadastrados
- ✅ Buscar livro por ISBN
- ✅ Buscar livro por título
- ✅ Deletar livro
- ✅ Persistência de dados em arquivo

---

## 🛠️ Tecnologias utilizadas

- Python
- JSON (para armazenamento de dados)

---

## 📂 Estrutura do Projeto

gerenciador-biblioteca/
│
├── main.py
├── menu.py
├── gerenciarBiblioteca.py
├── livro.py
├── validacao.py
├── excecoes.py
├── livros.txt
├── enums.py
├── gerarIsbn.txt

## ▶️ Como executar

1. Clone o repositório

## 💡 Como usar

Ao executar o programa, será exibido um menu com as opções:


1 - Cadastrar Livro
2 - Listar Livros
3 - Encontrar livro ISBN
4 - Encontrar livro título
5 - Deletar livro
6 - Sair


---

## 💾 Persistência de dados

Os dados são armazenados em um arquivo JSON (`livros.txt`), permitindo que as informações não sejam perdidas ao fechar o programa.
---

## ⚠️ Tratamento de erros

O sistema trata erros como:
- Livro não encontrado
- Arquivo inexistente
- Entradas inválidas
