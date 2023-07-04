# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Entre com a distancia em km: '))

if distancia < 200:
    preco_menor = distancia * 0.50
    print(f'O valor da passagem é {preco_menor}')

else:
    preco_maior = distancia * 0.45
    print(f'O valor da passagem é {preco_maior}')

