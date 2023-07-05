# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
# vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

atual = date.today().year

nasc = int(input('Entre com seu ano de nascimento: '))

if atual - nasc == 18:
    print('Você está na hora exata para se alistar')

if atual - nasc > 18:
    calc = (atual - nasc) - 18
    print(f'Você deveria ter se alistado a {calc} anos atrás')

if atual - nasc < 18:
    calc = (atual - nasc) - 18
    print(f'Você vai se alistar daqui a {abs(calc)} anos')


