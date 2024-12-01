#barbara e lucas
from Salaxd import SalaXD
from Salavip import SalaVIP
from Sala3d import Sala3D
from Sala import Sala


class cliente():
    
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def comprar(filme,tipo):
        match tipo:
            case 1:
                Sala.compra
        
            case 2:
                SalaVIP.compra
      
            case 3:
               SalaXD.compra
            case 3:
                Sala3D.compra
    
    def cancela_compra(filme,tipo):
        match tipo:
            case 1:
                Sala.exclui
            case 2:
                SalaVIP.exclui
            case 3:
                SalaXD.exclui
            case 4:
                Sala3D.exclui

for x in range(3):
    funcao = input("o que voce quer fazer? del(d)com(c)")
    if funcao== "c":
        print(list(enumerate(Sala.filmes)))
        filme = int(input("qual filme voce quer:\n"))
        tipo = int(input("que tipo de sala voce quer:\n 1 comumu\n 2 vip\n 3 xd\n 4 3d"))
        if 1<=tipo<=4:
            cliente.comprar(filme,tipo)
        else:
            print("essa sala nao existe")
    else:
        print(list(enumerate(Sala.filmes)))
        filme = int(input("qual filme voce escolheu:\n"))
        tipo = int(input("que tipo de sala voce escolheu?\n 1 comumu\n 2 vip\n 3 xd\n 4 3d"))
        if 1<=tipo<=4:
            cliente.cancela_compra(filme,tipo)
        else:
            print("essa sala nao existe")
    



             
             
        
       
