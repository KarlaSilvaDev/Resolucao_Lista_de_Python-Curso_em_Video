"""
Exercício Python 61:
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print('='*20)
print('GERADOR DE PA')
print('='*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print('{}'.format(termo) if cont == 1 else ' → {}'.format(termo), end='')
    termo += razao
    cont += 1
