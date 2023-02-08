# Faça um Programa que leia 3 notas e imprima a média delas.
total = 0
i = 0

for i in range (3):
    num = int(input("Entre com o número: "))
    total = total + num
    i+=1

media = total/3
print(media)


