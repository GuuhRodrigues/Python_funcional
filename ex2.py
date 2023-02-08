# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
import random

vetor = []

for i in range(5):
    vetor = int(random.randrange(0, 100))
    print(vetor)
