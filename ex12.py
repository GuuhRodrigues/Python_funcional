# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idade = []
altura = []
total = 0
media = 0
quantidade = 0

for i in range(30):
    idade.append(int(input("Entre com a idade: ")))
    altura.append(float(input("Entre com a altura: ")))
    total = total + altura[i]

media = total / 30

for i in range(30):
    if idade[i] > 13 and altura[i] < media:
        quantidade += 1

print("A quantidade de alunos com mais de 13 anos e altura inferior a média da turma é: ",quantidade)

