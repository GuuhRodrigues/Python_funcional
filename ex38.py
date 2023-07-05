#  Escreva um programa em Python que leia um número inteiro qualquer e
#  peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Entre com um número inteiro: '))

conv = int(input('Escolha qual será a base de conversão: \n(1) Binario\n(2) Octal\n(3) Hexadecimal\nOpção - '))

if conv == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)}')

elif conv == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')

else:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}')
