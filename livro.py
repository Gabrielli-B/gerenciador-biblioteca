import validacao
from gerarIsbn import gerarIsbn

class Livro:
    def __init__ (self,titulo,autor,anoPublicacao, genero,notaAvaliacao):
        validacao.validarAnoPublicacao(anoPublicacao)
        validacao.validarNotaAvaliacao(notaAvaliacao)
        validacao.validarGenero(genero)

        self.isbn = gerarIsbn()
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.genero = genero
        self.notaAvaliacao = notaAvaliacao

    def exibirDetalhes(self):
        print("ISBN.................... "+str(self.isbn))
        print("Titulo.................. "+self.titulo)
        print("Autor................... "+self.autor)
        print("Ano de Publicacao....... "+str(self.anoPublicacao))
        print("Genero.................. "+self.genero)
        print("Nota de avaliação....... "+str(self.notaAvaliacao))

    def to_dict(self):
        return{
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "anoPublicacao": self.anoPublicacao,
            "genero": self.genero,
            "notaAvaliacao": self.notaAvaliacao
        }

