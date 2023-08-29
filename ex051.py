"""
Exercício Python 51:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('='*30)
print('Progressão Aritmética')
print('='*30)
a1= int(input('Insira o valor do primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))

print('Primeiros 10 termos da PA:')
for c in range (a1, a1+r*10, r):
    print(c, end=' ')