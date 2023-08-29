
from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0, 5):
        n = randint(0, 10)
        lst.append(n)
        print(n, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lst}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)