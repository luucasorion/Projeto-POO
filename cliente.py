#barbara e lucas
from Sala import Sala
from Vip import VIP
from sala3d import Sala_3d
from xd import Xd
sala= Sala()
Vip = VIP()
sala_3d= Sala_3d()
sala_xd= Xd()

class cliente():
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def comprar(filme,tipo):
        if (tipo== 1):
            sala.imprimirSala(filme)
            assento = (list(map(int,input("escolha seu assento: ").split(" "))))
            sala.escolherAssento(filme,assento)
            sala.imprimirSala(filme)
        if (tipo== 2):
            Vip.imprimirSala(filme)
            assento = (list(map(int,input("escolha seu assento: ").split(" "))))
            Vip.escolherAssento(filme,assento)
            Vip.imprimirSala(filme)
        if(tipo==3):
            sala_xd.imprimirSala(filme)
            assento = (list(map(int,input("escolha seu assento: ").split(" "))))
            sala_xd.escolherAssento(filme,assento)
            sala_xd.imprimirSala(filme)
        if tipo == 4:
            sala_3d.imprimirSala(filme)
            assento = (list(map(int,input("escolha seu assento: ").split(" "))))
            sala_3d.escolherAssento(filme,assento)
            sala_3d.imprimirSala(filme)
    
    def cancela_compra(filme,tipo):
        if (tipo== 1):
            sala.imprimirSala(filme)
            assento = (list(map(int,input("escolha seu assento a ser deletado: ").split(" "))))
            sala.deleta_assento(filme,assento)
            sala.imprimirSala(filme)
        if (tipo== 2):
            Vip.imprimirSala(filme)
            assento = (list(map(int,input("escolha seu assento a ser deletado: ").split(" "))))
            Vip.deleta_assento(filme,assento)
            Vip.imprimirSala(filme)
        if(tipo==3):
            sala_xd.imprimirSala(filme)
            assento = (list(map(int,input("escolha seu assento a ser deletado: ").split(" "))))
            sala_xd.deleta_assento(filme,assento)
            sala_xd.imprimirSala(filme)
        if tipo == 4:
            sala_3d.imprimirSala(filme)
            assento = (list(map(int,input("escolha seu assento a ser deletado: ").split(" "))))
            sala_3d.deleta_assento(filme,assento)
            sala_3d.imprimirSala(filme)

for x in range(3):
    funcao = input("o que voce quer fazer? del(d)com(c)")
    if funcao== "c":
        print(list(enumerate(sala.filmes)))
        filme = int(input("qual filme voce quer:\n"))
        tipo = int(input("que tipo de sala voce quer:\n 1 comumu\n 2 vip\n 3 xd\n 4 3d"))
        if 1<=tipo<=4:
            cliente.comprar(filme,tipo)
        else:
            print("essa sala nao existe")
    else:
        print(list(enumerate(sala.filmes)))
        filme = int(input("qual filme voce escolheu:\n"))
        tipo = int(input("que tipo de sala voce escolheu?\n 1 comumu\n 2 vip\n 3 xd\n 4 3d"))
        if 1<=tipo<=4:
            cliente.cancela_compra(filme,tipo)
        else:
            print("essa sala nao existe")
    



             
             
        
       
