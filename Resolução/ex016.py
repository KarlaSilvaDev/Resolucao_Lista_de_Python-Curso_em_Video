"""
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção Inteira.
"""

"""
from math import trunc
num = float(input('Insira um número real: '))
print('A porção inteira do número {} é igual a {}'.format(num, trunc(num)))
"""

num = float(input('Insira um número real: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, int(num)))

