import random

def jogar():

    apresentacao_adivinhacao()

    numero_secreto = numero_aleatorio()
    print(numero_secreto)

    total_de_tentativas = 0
    pontos = 1000

    nivel = pede_nivel()

    if (nivel == 1):
        print("Você tem 20 tentativas, Boa Sorte\n!")
        total_de_tentativas = 20
    elif (nivel == 2):
        print("Você tem 10 tentativas, Boa Sorte!\n")
        total_de_tentativas = 10
    elif (nivel == 3):
        print("Você tem 5 tentativas, Boa Sorte!\n")
        total_de_tentativas = 5
    else:
        print("Opção Inválida !")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = pede_chute_adivinhacao()

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número de 1 e 100!\n")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            imprime_acertou_e_pontos_feitos(pontos)
            break
        else:
            if(menor):
                print("Você errou! Seu chute foi menor que o número secreto.\n")
            elif(maior):
                print("Você errou! O seu chute foi maior que o número secreto.\n")
            calculo_ponto_perdidos(numero_secreto, chute, pontos)
    if(acertou):
        imprime_mensagem_vencedor_adivinhacao()
    else:
        imprime_mensagem_perdedor_adivinhacao()

def apresentacao_adivinhacao():
    print("**********************************\n")
    print("Bem vindo ao jogo de adivinhação !\n")
    print("**********************************")

def numero_aleatorio():
    return random.randrange(1, 101)

def pede_nivel():
    print("Escolha o nível de dificuldade: \n")
    print("(1)Fácil (2)Médio (3)Difícil\n")
    nivel = input("Encolha o nível: ")
    nivel = int(nivel)
    print("")
    return nivel

def pede_chute_adivinhacao():
    chute = input("Digite o seu número entre 1 e 100: ")
    chute = int(chute)
    print("")
    return chute

def imprime_acertou_e_pontos_feitos(pontos):
    print("Você acertou e fez {} pontos!".format(pontos))

def calculo_ponto_perdidos(numero_secreto, chute, pontos):
    pontos_perdidos = abs(numero_secreto - chute)  # abs = absoluto sempre sera positivo
    pontos = pontos - pontos_perdidos

def imprime_mensagem_vencedor_adivinhacao():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor_adivinhacao():
    print("Acabou suas tentativas e voce perdeu !")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__=='__main__'):
    jogar()