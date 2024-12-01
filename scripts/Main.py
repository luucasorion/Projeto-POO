from Sala import Sala
from cliente import Cliente

sala = Sala()
cliente = Cliente()

class Main:
    def __init__(self):
        pass

    def main(self):        
        while True:
            escolha = input("""
            ===== Menu =====
            1. Comprar
            2. Mudar assento
            3. Cancelar Compra
            0. Sair
            =================
            """)

            match escolha:
                case '1':
                    sala.imprimir_filmes()
                    filme = int(input("Qual filme voce quer assistir?\n"))
                    tipo = int(input("""Escolha o tipo de sala que voce prefere: 
                    1. Sala Comum 
                    2. Sala VIP - Com cadeiras reclináveis e mais conforto 
                    3. Sala XD - Experiencia sonora aprimorada 
                    4. Sala 3D - Para uma imersão completa
                    Digite sua escolha: """))

                    if tipo < 1 or tipo > 4:                    
                        print("Essa sala não existe!")
                        continue
                    
                    cliente.comprar(filme, tipo)
                
                case '2':
                   
                    print("Opção de mudar assento ainda não implementada.")
                
                case '3':
                    sala.imprimir_filmes() 
                    filme = int(input("Qual filme voce escolheu?\n"))
                    tipo = int(input("""Que tipo de sala voce escolheu?
                    1. Sala Comum
                    2. Sala VIP
                    3. Sala XD
                    4. Sala 3D
                    Digite sua escolha: """))
                    
                    if 1 <= tipo <= 4:
                        cliente.cancela_compra(filme, tipo)
                    else:
                        print("Essa sala não existe")
                
                case '0':
                    print("Saindo do sistema...")
                    break 

                case _:
                    print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    meu_programa = Main() 
    meu_programa.main()  
