from Sessao import Sessao


class Assento():
    def __init__(self, assentos):
        self.assentos = [[0] * 15 for _ in range(15)]
    
    def escolherAssento(self, coordenada):
        self.assentos[coordenada[0]][coordenada[1]] = 1

        return self.assentos


