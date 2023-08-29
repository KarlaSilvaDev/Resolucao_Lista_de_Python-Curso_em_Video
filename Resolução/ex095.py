jogador = dict() # jogador = {nome: , gols:, total:} #temporária
gols = list() #temporária
time = list() #jogadores = [ {nome: , gols:, total:}, {nome: , gols:, total:}]

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for k in range(0, n):
        gols.append(int(input(f'   Quantos gols na partida {k+1}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
        if r not in 'SN':
            print('Resposta inválida.', end=' ')
        else:
            break
    if r == 'N':
        break

print('-='*40)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-'*40)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if n == 999:
        break
    elif n >= len(time):
        print(f'Não existe jogador com o código da busca.')
    else:
        print(f'--- LEVANTAMENTO do jogador {time[n]["nome"]}:')
        for k, v in enumerate(time[n]['gols']):
            print(f'  => Na partida {k + 1}, fez {v} gols. ')
    print('-'*40)
print('<<< VOLTE SEMPRE >>>')








