#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
total_notas =0
vetor = []
media = 0
contador =0

index = 0
ind = 0
for x in range(10):
    for i in range(4):
        notas = float(input("Entre com a {}º nota do {}º aluno:".format(index + 1, ind + 1)))
        total_notas += notas
        index += 1
    media = total_notas/4
    vetor.append(media)
    if media >= 7.0:
        contador +=1
    index -= 4
    ind += 1
print("A quantidade de alunos com média maior ou igual a 7.0 é ",contador)
print(vetor)

