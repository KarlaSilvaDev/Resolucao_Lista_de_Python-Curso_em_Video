from random import randint
from time import sleep
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'  O {k} tirou {v}')
    sleep(1)

print('=== Ranking dos jogadores ===')
cont = 1
for k in sorted(jogo, key = jogo.get, reverse= True):
    print(f'  {cont}º lugar: {k} com {jogo[k]}')
    cont += 1

#outra solução
from operator import itemgetter
ranking = dict()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
