""" Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""
from random import randint
aleatorio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')

maior = menor = cont = 0
for c in aleatorio:
    print(c, end=' ')
    if cont == 0:
        maior = menor = c
        cont += 1
    else:
        cont += 1
        if maior < c:
            maior = c
        if menor > c:
            menor = c
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')


# COM MÉTODOS DA TUPLA
print(f'\nO maior valor sorteado foi: {max(aleatorio)}')
print(f'O menor valor sorteado foi: {min(aleatorio)}')
