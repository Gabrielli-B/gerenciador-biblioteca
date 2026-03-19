import gerenciarBiblioteca
from enums import Genero
from excecoes import LivroNaoEncontradoError

def menuInformativo():
    print("\n========== Menu ==============")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Encontrar livro ISBN")
    print("4 - Encontrar livro título")
    print("5 - Deletar livro")
    print("6 - sair")

def menu():
    gerenciarBiblioteca.carregarLivrosArquivo()
    op = 0

    while op != 6:
        menuInformativo()
        op = int(input("escolha uma opção: "))

        if op == 1:
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            anoPublicacao = int(input("Ano publicação: "))
            notaAvaliacao =int(input("Nota avaliação: "))

            genero = input("Gênero: ").strip().upper()
            try:
                genero = Genero[genero]
            except KeyError:
                print("Genero inválido")
                continue

            gerenciarBiblioteca.cadastrarLivro(titulo,autor,anoPublicacao, genero,notaAvaliacao)
            gerenciarBiblioteca.escreverArquivo()

        elif op == 2:
            gerenciarBiblioteca.listarLivros()
        elif op == 3:
            isbn = int(input("Informe o ISBN: "))
            try:
                livro = gerenciarBiblioteca.encontrarLivroIsb(isbn)
                livro.exibirDetalhes()
            except LivroNaoEncontradoError as e:
                print(e)

        elif op == 4:
            titulo = input("Informe o título: ").strip()

            try:
                livro = gerenciarBiblioteca.encontrarLivroTitulo(titulo)
                livro.exibirDetalhes()
            except LivroNaoEncontradoError as e :
                print(e)

        elif op == 5:
            isbn = int(input("Informe o ISBN: "))
            try:
                gerenciarBiblioteca.deletarLivro(isbn)
                gerenciarBiblioteca.escreverArquivo()
            except LivroNaoEncontradoError as e:
                print(e)
        elif op == 6:
            print("Programa encerrado!")
        else:
            print("Opção inválida!")