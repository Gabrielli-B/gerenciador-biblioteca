from excecoes import NotaInvalidaError,AnoInvalidoError,GeneroInvalidoError
from datetime import datetime
from enums import Genero

def validarNotaAvaliacao(nota):
    if nota< 0 or nota>10:
         raise NotaInvalidaError("Nota inválida")
    
def validarAnoPublicacao(ano):
     anoAtual = datetime.now().year
     if ano < 1400 or ano > anoAtual:
          raise AnoInvalidoError("Ano de publicação inválido")
    
def validarGenero(genero):
     if not isinstance(genero,Genero):
          raise GeneroInvalidoError("Gênero inválido")

