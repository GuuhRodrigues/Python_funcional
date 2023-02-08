# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

vetor_perguntas = ["Telefonou para a vítima ? ", "Esteve no local do crime ? ", "Mora perto da vítima ? ", "Devia para a vítima ? ", "Já trabalhou com a vítima ? "]
quant = 0
index = 0

for i in range(5):
    print(vetor_perguntas[index])
    resposta = str(input("Resposta: "))
    resposta.lower()

    if resposta == "sim":
        quant += 1
        index += 1

    elif resposta != "sim" and resposta != "não":
        print("Resposta inválida! Responda (sim) ou (não)")

    else:
        index += 1
        continue

if quant == 2:
    print("Suspeita")

elif quant >=3 and quant <=4:
    print("Cúmplice")

elif quant == 5:
    print("Assassino")

else:
    print("Inocente")





