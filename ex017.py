"""
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

"""from math import sqrt, pow
cateto_oposto = float(input('Digite o comprimento do cateto oposto em centímetros: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente em centímetros: '))
hipotenusa = sqrt(pow(cateto_oposto,2)+pow(cateto_adjacente,2))
print('O triângulo retângulo com cateto oposto de {:.1f}cm e cateto adjacente de {:.1f}cm possui uma hipotenusa de {:.1f}cm.'.format(cateto_oposto, cateto_adjacente, hipotenusa))"""

from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto em centímetros: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente em centímetros: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('O triângulo retângulo com cateto oposto de {:.1f}cm e cateto adjacente de {:.1f}cm possui uma hipotenusa de {:.1f}cm.'.format(cateto_oposto, cateto_adjacente, hipotenusa))