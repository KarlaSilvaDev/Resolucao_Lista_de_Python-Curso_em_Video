"""
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians
#as funções importadas esperam que o ângulo esteja em radianos
angulo = float(input('Insira um ângulo: '))
angulo_rad = radians(angulo)
print('Para o ângulo de {}°, temos: \nsen = {:.2f}\ncos = {:.2f}\ntan = {:.2f}'.format(angulo, sin(angulo_rad), cos(angulo_rad), tan(angulo_rad)))


