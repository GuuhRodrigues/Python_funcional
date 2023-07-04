# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice # choice serve pra escolher um da 'lista'

vetor = []

for i in range(0,4):
    vetor.append(str(input(f'Entre com o {i + 1}º aluno: ')))

escolhido = choice(vetor)

print(f'O escolhido foi o aluno(a) {escolhido}')


