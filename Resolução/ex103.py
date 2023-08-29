def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols.isdigit() == False:
        gols = '0'
    return print(f'O jogador {nome.title().strip()} fez {gols.strip()} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
ficha(n, g)