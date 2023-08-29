"""
Exercício Python 52:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print('='*40)
print('Determinando se um número é primo')
print('='*40)
num = int(input('Número a ser analisado: '))
soma = 0
for c in range(num, 0, -1):
    if num % c == 0:
        soma = soma + 1
if soma == 2:
    print('O número {} é primo!'.format(num))
else:
    print('O número {} não é primo!'.format(num))