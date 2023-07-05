# Faça um programa que leia três números inteiros e mostre qual é o maior e qual é o menor.

num = []
maior = 0
menor = 0
for i in range(0,3):
    num.append(int(input(f'Entre com o {i+1}º números: ')))

    if num[i] > maior:
        maior = num[i]
    else:
        menor = num[i]

print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
