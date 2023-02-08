        # Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
temp = []
total = 0
media  = 0
for i in range(12):
    temp.append(int(input("Entre com a temperatura média do mês de {}: ".format(mes[i]))))
    total += temp[i]

media = total/12

for i in range(12):
    if temp[i] > media:
        print("Temperaturas acima da média anual: ", temp[i])
        print("{} ".format(mes[i]))
