jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for k in range(0, n):
    partidas.append(int(input(f'Quantos gols na partida {k + 1}? ')))
jogador['gols'] = partidas.copy()
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'  => Na partida {k+1}, fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols.')



