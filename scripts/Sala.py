
#barbara
from _typeshed import Self


class Sala:
    def __init__(self):
        self.filmes = ["filme1", "filme2", "filme3"]
        self.salas = [[[0] * 4 for _ in range(4)] for _ in range(3)]
        self.preco = 30

    def ImprimirSala( self,coordenadas):
        for matriz in self.salas[coordenadas]:
            print(matriz)

    def OcuparAssento(self, coordenadas, assento):
        if self.salas[coordenadas][assento[0]][assento[1]] == 0:
            self.salas[coordenadas][assento[0]][assento[1]] = 1
            print("preco do seu ingresso foi: ",self.preco)
        else:
            print("Assento já ocupado!")
    
    def Deletar_assento(self, coordenadas, assento):
        if self.salas[coordenadas][assento[0]][assento[1]] == 1:
            self.salas[coordenadas][assento[0]][assento[1]] = 0
            print("compra cancelada com sucesso!")
        else:
            print("Assento não está ocupado!")
      
        
    def adiciona(self, tipo, filme):
        self.imprimirSala(filme)
        assento = (list(map(int,input("escolha seu assento: ").split(" "))))
        self.escolherAssento(filme,assento)
        self.imprimirSala(filme)
        
    def exclui(self, tipo, filme):
        self.imprimirSala(filme)
        assento = (list(map(int,input("escolha seu assento a ser deletado: ").split(" "))))
        self.deleta_assento(filme,assento)
        self.imprimirSala(filme)