# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Entre com o salário do funcionario: R$'))

if salario > 1250:
    aum = salario * 10 / 100
    newsal = salario + aum
    print(f'O salario do funcionario após o aumento de 10% é de R${newsal}')

else:
    aum = salario * 15 / 100
    newsal = salario + aum
    print(f'O salario do funcionario após o aumento de 15% é de R${newsal}')

