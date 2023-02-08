# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor = []
vetor_2 = []
vetor_3 = []

for i in range(10):
    vetor.append(int(input("Entre com os elementos do primeiro vetor: ")))
    vetor_2.append(int(input("Entre com os elementos do segundo vetor: ")))
    vetor_3.append(vetor[i])
    vetor_3.append(vetor_2[i])

print("Elementos dos dois vetores intercalados :", vetor_3)
