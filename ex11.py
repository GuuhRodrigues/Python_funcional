# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada

vetor = []
vetor_2 = []
vetor_3 = []
vetor_4 = []

for i in range(10):
    vetor.append(int(input("Entre com os elementos do primeiro vetor: ")))
    vetor_2.append(int(input("Entre com os elementos do segundo vetor: ")))
    vetor_3.append(int(input("Entre com os elementos do terceiro vetor: ")))
    vetor_4.append(vetor[i])
    vetor_4.append(vetor_2[i])
    vetor_4.append(vetor_3[i])
print("Elementos dos três vetores intercalados :", vetor_4)
