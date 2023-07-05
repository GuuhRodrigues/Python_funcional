# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

seg = []
menor = 0
maior = 0
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
for i in range(0,3):
    seg.append(int(input(f'Entre com o {i+1}º seguimento: ')))

if seg[0] < seg[1] + seg[2] and seg[1] < seg[0] + seg[2] and seg[2] < seg[0] + seg[1]:
    print('Sim, esses seguimentos podem formar um triângulo')
else:
    print('Não, esses seguimentos não formam um triângulo')





