import validacao

class Livro:
    def __init__ (self,titulo,autor,anoPublicacao,genero,notaAvaliacao):
        validacao.validarAnoPublicacao(anoPublicacao)
        validacao.validarNotaAvaliacao(notaAvaliacao)
        
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.genero = genero
        self.notaAvaliacao = notaAvaliacao

    def exibirDetalhes(self):
        print("Titulo.................. "+self.titulo)
        print("Autor................... "+self.autor)
        print("Ano de Publicacao....... "+str(self.anoPublicacao))
        print("Genero.................. "+self.genero)
        print("Nota de avaliação....... "+str(self.notaAvaliacao))


