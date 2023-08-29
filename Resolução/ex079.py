"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
num = list()
c = 0
while True:
    n = int(input(f'Digite o {c+1}º número: '))
    if n not in num:
        num.append(n)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar!')
    while True:
        resp = str(input(f'Deseja continuar? [S/N] ')).strip()[0].upper()
        if resp in 'SN':
            break
        else:
            print('Resposta inválida! ', end='')
    if resp == 'N':
        break
    c += 1
num.sort()
print(f'Você digitou os valores {num}')
