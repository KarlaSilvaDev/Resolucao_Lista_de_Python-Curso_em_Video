"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
turma = []
dados = []
#ENTRADA DE DADOS
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[-1]+dados[-2])/2)
    turma.append(dados[:])
    dados.clear()
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
        if r not in 'SN':
            print('Resposta inválida. ', end='')
        else:
            break
    if r == 'N':
        break
#TABELA COM AS MÉDIAS
print('-='*30)
for c in range(0, len(turma)):
    if c == 0:
        print(f'{"No.":<5}{"NOME":<15}{"MÉDIA":>5}')
        print('-'*25)
    print(f'{c+1:<5}{turma[c][0]:<15}{turma[c][3]:>5.2f}')
print('-'*30)

#MOSTRANDO AS NOTAS INDIVIDUAIS
while True:
    c = int(input('Mostrar notas de qual aluno?(999 interrompe) Número: '))
    if c == 999:
        break
    else:
        if c <= (len(turma)):
            print('-'*30)
            print(f'Notas de {turma[c-1][0]} são {turma[c-1][1:3]}')
            print('-' * 30)
        else:
            print('Número de aluno inválido. ', end='')

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

