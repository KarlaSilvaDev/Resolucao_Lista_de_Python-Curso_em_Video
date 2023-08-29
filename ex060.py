"""
Exercício Python 060:
Faça um programa que leia um número qualquer e mostre o seu fatorial.

"""
from time import sleep
print('---CÁLCULO DO FATORIAL---')
num = int(input('Digite um número inteiro:'))
print('Calculando...')
sleep(2)
cont = num
fatorial = 1
print('{}! = '.format(num), end='')
while cont > 0:
    fatorial *= (cont)
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ',end='')
    cont -= 1
print(fatorial)

