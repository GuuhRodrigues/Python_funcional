# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# – O primeiro valor é maior – O segundo valor é maior – Não existe valor maior, os dois são iguais

valores = []

for i in range(0, 2):
    valores.append(int(input(f'Entre com o {i+1}º número inteiro: ')))

if valores[0] > valores[1]:
    print('O primeiro valor é maior')

elif valores[1] > valores[0]:
    print('O segundo valor é maior')

else:
    print('Não existe valor maior, os dois são iguais')
