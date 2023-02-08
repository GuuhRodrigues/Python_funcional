#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante

vendedores = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(9):
    venda = float(input("Valor das vendas: "))
    salario = (venda * 9)/100 + 200

    indice = int(salario/100) - 1
    if indice > 9:
        indice = 9
    else:
        indice = 1

    vendedores[indice - 1] += 1

for i in range(9):
    print("%d - %d : %d " % (i * 100 + 200, (i + 1) * 100 + 199, vendedores[i]))

