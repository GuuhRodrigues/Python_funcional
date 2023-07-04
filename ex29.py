#  Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
#  descobrir qual foi o número escolhido pelo computador.
#  O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

num = random.randrange(0, 6)

while True:
    tente = int(input('Tenta descobrir o número de 0 à 5: '))
    if tente == num:
        print('Parabén voce acertou =)')
        break
    else:
        print('Você Errou =/ ')


