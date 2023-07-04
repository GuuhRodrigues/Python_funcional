# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

vetor = []

for i in range(0, 4):
    vetor.append(str(input(f'Entre com os nomes dos alunos: ')))

shuffle(vetor)

print(f'A ordem da apresentação dos trabalhos será {vetor}')
