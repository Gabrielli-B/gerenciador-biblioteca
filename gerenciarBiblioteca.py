import livro
from excecoes import LivroNaoEncontradoError

listaLivros = {}

def cadastrarLivro(titulo,autor,anoPublicacao, genero,notaAvaliacao):
    novoLivro = livro.Livro(titulo,autor,anoPublicacao,genero,notaAvaliacao) 
    listaLivros[novoLivro.isbn] = novoLivro

def listarLivros():
    for livros in listaLivros.values():
        livros.exibirDetalhes()

def encontrarLivroIsb(isbn):
    if isbn in listaLivros:
        return listaLivros[isbn]
    raise LivroNaoEncontradoError("Livro não foi encontrado")

def encontrarLivroTitulo(titulo):
    if livro in listaLivros.values():
        if livro.titulo.lower() == titulo.lower():
            return livro
    else:
        raise LivroNaoEncontradoError("Livro não foi encontrado")

def deletarLivro(isbn):
    encontrarLivroIsb(isbn)
    del listaLivros[isbn]