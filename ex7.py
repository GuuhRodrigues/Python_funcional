#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = []
soma = 0
mult = 1
for i in range(5):
    num = int(input("Entre com {}º número: ".format(i+1)))
    vetor.append(num)
    soma += num
    mult = mult * num

print("Os números são: ", vetor)
print("A soma deles é ", soma)
print("A multiplicação é ", mult)