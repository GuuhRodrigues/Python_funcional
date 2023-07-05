# Crie um programa que faça o computador jogar Jokenpô com você.
import random
jok = random.randrange(0, 3)
print(jok)
while True:

    pessoa = int(input('Opções: \n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\nJÓ KEN PÔ! '))
    if jok != pessoa:
        if pessoa == 0 and jok == 2:
            print('Você venceu ! Pedra quebrou a teroura ;)')

        elif pessoa == 1 and jok == 0:
            print('Você venceu ! Papel engoliu a pedra ;)')

        elif pessoa == 2 and jok == 1:
            print('Você venceu ! Tesoura cortou o papel ;)')

        elif jok == 0 and pessoa == 2:
            print('Você perdeu ! Pedra quebrou a tesoura :/ ')

        elif jok == 1 and pessoa == 0:
            print('Você perdeu ! Papel engoliu a pedra :/ ')

        elif jok == 2 and pessoa == 1:
            print('Você perdeu ! Tesoura cortou o papel :/ ')
        break
    else:
        print('Vocês empataram, tente novamente ...')




