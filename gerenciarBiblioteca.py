import livro
from excecoes import LivroNaoEncontradoError

listaLivros = {}

def cadastrarLivro(titulo,autor,anoPublicacao, genero,notaAvaliacao):
    novoLivro = livro.Livro(titulo,autor,anoPublicacao,genero,notaAvaliacao) 
    listaLivros[novoLivro.isbn] = novoLivro

def listarLivros():
    for livros in listaLivros.values():
        livros.exibirDetalhes()

def encontrarLivro(isbn):
    if isbn in listaLivros:
        return listaLivros[isbn]
    raise LivroNaoEncontradoError("Livro não foi encontrado")