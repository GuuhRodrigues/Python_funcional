#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Entre com o valor da casa: '))
salario = float(input('Entre com o salario do comprador: '))
anos = int(input('Entre com quantos anos ele vai pagar: '))

valor = casa / (anos * 12)

if valor <= salario * 30 /100:
    print('O emprestimo foi aprovado !')

else:
    print('O emprestimo foi negado.')
