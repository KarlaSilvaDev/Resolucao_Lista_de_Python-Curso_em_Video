"""
Exercício Python 54:
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
maior_idade = 0
menor_idade = 0
ano_atual = date.today().year
for c in range(1,8):
    ano = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    if ano_atual - ano >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print('Quantidade de pessoas maiores de idade: {}'.format(maior_idade))
print('Quantidade de pessoas menores de idade: {}'.format(menor_idade))
