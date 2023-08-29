"""
Exercício Python 28:
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
print('-=-'*18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-'*18)
pc = randint(0, 5)
print(pc)
user = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if pc == user:
    print('Você venceu!')
else:
    print('Você perdeu! Eu pensei no número {} e não no número {}!'.format(pc, user))