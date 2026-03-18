import livro
import json
from enums import Genero
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
    for livro in listaLivros.values():
        if livro.titulo.lower() == titulo.lower():
            return livro
    else:
        raise LivroNaoEncontradoError("Livro não foi encontrado")

def deletarLivro(isbn):
    encontrarLivroIsb(isbn)
    del listaLivros[isbn]
    print("Livro deletado com sucesso!")

def escreverArquivo():
    arquivo = open("livros.txt","w")
    dados = {}
    for isbn, livro in listaLivros.items():
        dados[isbn] = livro.to_dict()

    json_string = json.dumps(dados)
    arquivo.write(json_string)

    arquivo.close()

def carregarLivrosArquivo():
    try:
        arquivo = open("livros.txt","r")
        dados = json.load(arquivo)
        arquivo.close()

        global listaLivros
        listaLivros={}

        for isbn, info in dados.items():
            novoLivro = livro.Livro(
                info["titulo"],
                info["autor"],
                info["anoPublicacao"],
                Genero(info["genero"]),
                info["notaAvaliacao"]
            )
            novoLivro.isbn = isbn
            listaLivros[isbn] = novoLivro
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum livro foi carregado.")