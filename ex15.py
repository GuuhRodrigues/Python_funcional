#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

notas = []
media = 0
acima = 0
abaixo = 0

while True:
    nota = float(input("Entre com as notas: "))
    if nota == -1:
        print("Programa encerrado\n")
        break
    notas.append(nota)

print("Quantidade de valores: ", len(notas))

print("Valores na ordem: ", notas)

notas.reverse()
print("Valores ordem inversa e um abaixo do outro: \n", notas, "\n")

print("A soma dos valores é: ", sum(notas))

media = sum(notas)/len(notas)
print("A média dos valores é: ", media)

if nota in notas:
    if nota > media:
        acima += 1
        print("Quantidade de valores acima da média: ", acima)

    if nota < 7.0:
        abaixo += 1
        print("Quantidade de valores abaixo de sete: ", abaixo)

print("Obrigado por utilizar o programa, até mais :) ")