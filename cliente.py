import copy
class sala():
    def __init__(self, filmes, salas, preco):
        self.filmes = ["filme1","filme2","filme3"]
        self.salas = [[[0]*4 for _ in range(4)]for _ in range(3)]
        self.preco= 30
    def imprimirSala(self,coordenadas):
        for matriz in self.salas[coordenadas]:
            print(matriz)
    def escolherAssento(self,coordenadas, assento):
        self.salas[coordenadas][assento[0][assento[1]]]= 1


class vip():
    def __init__(self, salas):
        salas_vip = copy.deepcopy(salas)
        super().__init__(salas_vip)
        self.preco_vip=self.preco
    def acresimo(self):
        self.preco_vip*=1,45


class sala3d():
     def __init__(self, salas):
        salas_vip = copy.deepcopy(salas)
        super().__init__(salas_vip)
        self.preco_3d=self.preco
   
     def acresimo(self):
        self.preco_3d*=1,30

class sala_xd():
    def __init__(self, salas):
        salas_vip = copy.deepcopy(salas)
        super().__init__(salas_vip)
        self.preco_xd=self.preco
   
    def acresimo(self):
        self.preco_xd*=1,40

class cliente ():
    def __init__(self, nome, idade):
        self.nome =nome
        self.idade= idade
    def imprimirSalas(self,tipoDeSala):
      x = vip
      x.im          
         

        