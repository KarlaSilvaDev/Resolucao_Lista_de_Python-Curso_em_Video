"""
Exercício Python 071:
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('='*31)
print(' '*10,'BANCO CEV',' '*10)
print('='*31)

valor = float(input('Que valor você quer sacar? R$'))
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print('Total de {} cédulas de R${:.2f}'.format(totced, ced))
        if valor >= 20:
            ced = 20
        elif valor >= 10:
            ced = 10
        elif valor >= 1:
            ced = 1
        totced = 0
        if valor == 0:
            break
