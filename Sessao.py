from Assento import Assento
from Sessoes import Sessoes

class Sessao():
    def __init__(self, filme):
        self.filme = filme
        
    
    def EscolherAcento(self, coordenada):
        Sessoes.adicionarMatriz()
        
        Assento.escolherAssento(coordenada)