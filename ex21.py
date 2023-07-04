# Crie um programa que leia o nome completo de uma pessoa e mostre: – O nome com todas as letras maiúsculas e
# minúsculas; – Quantas letras ao todo (sem considerar espaços). – Quantas letras tem o primeiro nome.

nome = (str(input('Escreva seu nome completo: '))).strip()
print(nome)

print(f'Nome maiúsculo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras ao todo')
#print(f'Seu primeiro nome tem {nome.find(" ")} letras')

separa = nome.split()
print(f'Seu primeiro nome tem {len(separa[0])} letras')






