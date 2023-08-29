"""
Exercício Python 68:
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.
"""
from random import randint
print('='*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*25)
cont = 0
while True:
    user = int(input('Diga um valor: '))
    while True:
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip()[0].upper()
        if tipo in 'PI':
            break
    pc = randint(0, 10)
    soma = pc + user
    print(f'\033[1;30;43m Você jogou {user} e o computador {pc}. Total de {soma} ', 'DEU PAR\033[m' if soma % 2 == 0 else 'DEU ÍMPAR\033[m')
    if (soma % 2 == 0 and tipo == 'P') or (soma % 2 != 0 and tipo == 'I'):
        print('\033[1;30;46m VOCÊ VENCEU!\033[m')
        cont += 1
    else:
        print('\033[1mVOCÊ PERDEU!\033[m')
        break
print(f'GAME OVER! Você venceu {cont} vez(es).')