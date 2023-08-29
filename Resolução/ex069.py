"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
idadeMais18 = totalHomens = totalMulheres = 0
while True:
    print('-'*25)
    print('   CADASTRE UMA PESSOA   ')
    print('-'*25)
    idade = int(input('Idade: '))
    if idade > 18:
        idadeMais18 += 1
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip()[0].upper()
        if sexo in 'MF':
            if sexo == 'M':
                totalHomens += 1
            else:
                if idade < 20:
                    totalMulheres += 1
            break
        else:
            print('Resposta inválida!')
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
        if resp in 'SN':
            break
        else:
            print('Resposta inválida!')
    if resp == 'N':
        break
print('Total de maiores de 18 anos: {}'.format(idadeMais18))
print('Total de homens cadastrados: {}'.format(totalHomens))
print('Total de mulheres com menos de 20 anos: {}'.format(totalMulheres))

