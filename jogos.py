import adivinhacao
import forca

def escolha_jogo():

    print("**********************************\n")
    print("  Escolha o jogo que quer jogar!  \n")
    print("**********************************\n")
    print("     (1)Adivinhação (2)Forca        ")

    jogo = int(input("Qual jogo: "))

    if(jogo == 1):
        adivinhacao.jogar()
    elif(jogo == 2):
        forca.jogar()
    else:
        print("Opção Inválida")
if(__name__ == "__main__"):
    escolha_jogo()