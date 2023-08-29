"""
Exercício 25:
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""

name = str(input('Insira o seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in name.upper()))