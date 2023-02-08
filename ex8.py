#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida

vetor_idade = []
vetor_altura = []

for i in range(5):
    idade = int(input("Entre com a idade: "))
    altura = float(input("Entre com a altura: "))

    vetor_idade.append(idade)
    vetor_altura.append(altura)

vetor_idade.reverse() #inverter idade
print("Idades: ", vetor_idade)
vetor_altura.reverse() #inverter altura
print("Alturas:", vetor_altura)

