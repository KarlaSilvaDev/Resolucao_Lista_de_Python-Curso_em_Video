"""
Exercício Python 35:
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
"""

print('Insira o comprimento das retas em centímetros:')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('As retas formam um triângulo.')
else:
    print('As retas não formam um triângulo.')