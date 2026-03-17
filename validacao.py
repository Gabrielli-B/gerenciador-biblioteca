from excecoes import NotaInvalidaError,AnoInvalidoError
from datetime import datetime

def validarNotaAvaliacao(nota):
    if nota< 0 or nota>10:
         raise NotaInvalidaError("Nota inválida")
    
def validarAnoPublicacao(ano):
     anoAtual = datetime.now().year
     if ano < 1400 or ano > anoAtual:
          raise AnoInvalidoError("Ano de publicação inválido")
     
