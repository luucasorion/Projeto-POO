#barbara e lucas
from Salaxd import SalaXD
from Salavip import SalaVIP
from sala3d import Sala3D
from Sala import Sala

sala = Sala()
salaVIP = SalaVIP()
sala3D = Sala3D()
salaXD = SalaXD()


class Cliente():
    
    def __init__(self):
        pass

    def comprar(self, filme, tipo):
        match tipo:
            case 1:
                sala.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                sala.OcuparAssento(filme, assento)   
            case 2:         
                salaVIP.ImprimirSala(filme)
                assento = [int(x) for x in input("escolha seu assento: ").split(" ")]
                salaVIP.OcuparAssento(filme, assento)
            case 3:
                salaXD.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                salaXD.OcuparAssento(filme, assento)
            case 3:
                sala3D.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                sala3D.OcuparAssento(filme, assento)

    
    def cancela_compra(self, filme, tipo):
        match tipo:
            case 1:
                sala.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                sala.Deletar_assento(filme, assento)   
            case 2:         
                salaVIP.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                salaVIP.Deletar_assento(tipo, filme)
            case 3:
                salaXD.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                salaXD.Deletar_assento(tipo, filme)
            case 3:
                sala3D.ImprimirSala(filme)
                assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                sala3D.Deletar_assento(tipo, filme)

    def atualizarAssento(self, filme, tipo):
            match tipo:
                case 1:
                    sala.ImprimirSala(filme)
                    assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                    assentoNovo = (list(map(int,input("escolha seu novo assento: ").split(" "))))
                    sala.Atualizar(filme, assento, assentoNovo)   
                case 2:         
                    salaVIP.ImprimirSala(filme)
                    assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                    assentoNovo = (list(map(int,input("escolha seu novo assento: ").split(" "))))
                    salaVIP.Atualizar(filme, assento, assentoNovo)   
                case 3:
                    salaXD.ImprimirSala(filme)
                    assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                    assentoNovo = (list(map(int,input("escolha seu novo assento: ").split(" "))))
                    salaXD.Atualizar(filme, assento, assentoNovo)   
                case 3:
                    sala3D.ImprimirSala(filme)
                    assento = (list(map(int,input("escolha seu assento: ").split(" "))))
                    assentoNovo = (list(map(int,input("escolha seu novo assento: ").split(" "))))
                    sala3D.Atualizar(filme, assento, assentoNovo)   
    
    def visualizar(self, filme, tipo):
        match tipo:
            case 1:
                sala.ImprimirSala(filme)
                
            case 2:         
                salaVIP.ImprimirSala(filme)
               
            case 3:
                salaXD.ImprimirSala(filme)
               
            case 3:
                sala3D.ImprimirSala(filme)
                


             
             
        
       
