#barbara

class Sala:
    def __init__(self):
        self.filmes = ["filme1", "filme2", "filme3"]
        self.salas = [[[0] * 4 for _ in range(4)] for _ in range(3)]
        self.preco = 30

    def ImprimirSala(self,filme):
        for matriz in self.salas[filme]:
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
           
        else:
            print("Assento não está ocupado!")
      
        
    
        
   

    def ImprimirFilmes(self):
        for x in range(len(self.filmes)):
            print(f"{x} - {self.filmes[x]}")

    def Atualizar(self, filme, assento, assentoNovo):
        self.Deletar_assento(filme, assento)
        self.OcuparAssento(filme, assentoNovo)
        