# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

contador = 0
consoantes = []

index=0
for i in range(10):
    letras = str(input("Entre com a letra: ").strip())
    letras = letras.upper()

    if letras not in "AEIOU":
        contador += 1
        consoantes.append(letras)
        print("Foram lidas ", contador, " consoantes e são elas: ", consoantes)
index+=1









