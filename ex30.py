# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Entre com a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado no valor de {multa:.2f}')

else:
    print('Você está dentro da velocidade limite da via')