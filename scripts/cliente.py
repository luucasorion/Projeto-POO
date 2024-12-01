#barbara e lucas
from Salaxd import SalaXD
from Salavip import SalaVIP
from Sala3d import Sala3D
from Sala import Sala

sala = Sala()
salaVIP = SalaVIP()
sala3D = Sala3D()
salaXD = SalaXD()


class Cliente():
    
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def comprar(filme,tipo):
        match tipo:
            case 1:
                sala.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                sala.Adicionar(tipo, filme)   
            case 2:         
                salaVIP.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                salaVIP.Adicionar(tipo, filme)
            case 3:
                salaXD.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                salaXD.Adicionar(tipo, filme)
            case 3:
                sala3D.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                sala3D.Adicionar(tipo, filme)

    
    def cancela_compra(filme,tipo):
        match tipo:
            case 1:
                sala.Excluir(tipo, filme)
            case 2:
                salaVIP.Excluir(tipo, filme)
            case 3:
                salaXD.Excluir(tipo, filme)
            case 4:
                sala3D.Excluir(tipo, filme)





             
             
        
       
