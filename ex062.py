"""
Exercício Python 62:
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
print('='*20)
print('GERADOR DE PA')
print('='*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
maisTermos = 10
total = 0
while maisTermos != 0:
    total += maisTermos
    while cont <= total:
        print('{} → '.format(termo), end='')
        cont += 1
        termo += razao
    print('PAUSA')
    maisTermos = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')

