"""
Exercício Python 50:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('{}° número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} número(s) PAR(ES) e a soma é igual a {}.'.format(cont, soma))