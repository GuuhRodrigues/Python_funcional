# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Entre com o ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'O ângulo {ang} tem o seno igual a {seno:.2f}, o cosseno valendo {cos:.2f} e o tangente igual a {tan:.2f} ')
