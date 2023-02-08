# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
vetor_par = []
vetor_impar = []

for i in range(20):
    numero = int(input("Entre com os numeros:"))
    vetor.append(numero)
    if numero % 2==0:
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)

print("Vetor completo :", vetor)
print("Vetor par: ", vetor_par)
print("Vetor impar: ", vetor_impar)