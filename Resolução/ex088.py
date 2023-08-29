from random import randint
from time import sleep
jogos = []
print('-'*30)
print('     JOGA NA MEGA SENA     ')
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=')
for l in range(0, n):
    jogos.append([])
    while len(jogos[l]) < 6:
        num = randint(1, 60)
        if num not in jogos[l]:
            jogos[l].append(num)
    print(f'{l+1}º jogo: {sorted(jogos[l])}')
    sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)
