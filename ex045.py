"""
Exercício Python 45:
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep
print('-=-'*8)
print('JOKENPÔ GAME')
print('-=-'*8)
itens = ('Pedra', 'Papel', 'Tesoura')
user = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\nEscolha uma opção: '))
pc = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}.'.format(itens[pc]))
print('Jogador jogou {}.'.format(itens[user]))
print('-='*11)
if pc == 0:
    if user == 0:
        print('Resultado: EMPATE')
    elif user == 1:
        print('Resultado: VOCÊ VENCEU!')
    elif user == 2:
        print('Resultado: VOCÊ PERDEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1:
    if user == 0:
        print('Resultado: VOCÊ PERDEU')
    elif user == 1:
        print('Resultado: EMPATE!')
    elif user == 2:
        print('Resultado: VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
else:
    if user == 0:
        print('Resultado: VOCÊ VENCEU!')
    elif user == 1:
        print('Resultado: VOCÊ PERDEU!')
    elif user == 2:
        print('Resultado: EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
