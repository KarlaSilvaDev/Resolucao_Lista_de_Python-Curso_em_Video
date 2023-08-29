"""
Exerícioc Python 63:
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci
"""
print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)
total = int(input('Quantos termos você deseja mostrar? '))
termo1 = 1
termo2 = 1
cont = total
while cont != 0:
    if cont == total or cont == (total - 1):
        print('{} → '.format(termo1), end = '')
    else:
        termo3 = termo1 + termo2
        print('{} → '.format(termo3), end = '')
        termo1 = termo2
        termo2 = termo3
    cont -= 1
print('FIM')
