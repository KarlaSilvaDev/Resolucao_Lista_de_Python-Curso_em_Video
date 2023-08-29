"""
Exercício Python 58:
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
 foram necessários para vencer.
"""
from random import randint
pc = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10! Tente adivinhar!')
user = int(input('Qual é o seu palpite? '))
cont = 1
while user != pc:
    if user > pc:
        print('Menos...', end = '')
    else:
        print('Mais...', end = '')
    user = int(input('Tente novamente: '))
    cont += 1
print('-=-'*20)
print('ACERTOU! \nNúmero escolhido pelo computador: {}\nNúmero de tentativas até o usuário acertar: {}'.format(pc, cont))
print('-=-'*20)
