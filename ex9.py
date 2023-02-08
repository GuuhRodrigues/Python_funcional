# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = []
quadrado = 0
soma = 0

for i in range(10):
    num = int(input("Entre com os números: ").strip())
    quadrado = num**2
    soma += quadrado

print("A soma do quadrado dos números é ", soma)

