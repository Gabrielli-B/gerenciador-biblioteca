import gerenciarBiblioteca
from enums import Genero

def menuInformativo():
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
            titulo = input("Título: ")
            autor = input("Autor: ")
            anoPublicacao = int(input("Ano publicação: "))
            notaAvaliacao =int(input("Nota avaliação: "))

            genero = input("Gênero: ").upper()
            try:
                genero = Genero[genero]
            except KeyError:
                print("Genero inválido")
                continue

            gerenciarBiblioteca.cadastrarLivro(titulo,autor,anoPublicacao, genero,notaAvaliacao)
            gerenciarBiblioteca.escreverArquivo()

        elif op == 2:
            gerenciarBiblioteca.listaLivros()
        elif op == 3:
            isbn = int(input("Informe o ISBN: "))
            livro = gerenciarBiblioteca.encontrarLivroIsb(isbn)
            livro.exibirDetalhes()
        elif op == 4:
            titulo = input("Informe o título: ")
            livro = gerenciarBiblioteca.encontrarLivroTitulo(titulo)
            livro.exibirDetalhes()
        elif op == 5:
            isbn = int(input("Informe o ISBN: "))
            gerenciarBiblioteca.deletarLivro(isbn)
        else:
            print("Opção inválida!")