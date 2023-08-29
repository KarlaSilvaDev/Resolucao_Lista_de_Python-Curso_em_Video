"""
Exercício 27:
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
"""

name = str(input('Digite o seu nome completo: ')).strip()

print('Seu primeiro nome é {}.'.format(name.split()[0]))

print('Seu último número é {}.'.format(name.split()[len(name.split())-1]))
