"""
Exercício Python 39:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do
prazo.
"""
from datetime import date
ano = int(input('Insira o seu ano de nascimento com 4 caracteres: '))
idade = date.today().year - ano
if idade == 18:
    print('É hora de se alistar.')
elif idade < 18:
    print('Você deve se alistar daqui a {} ano(s).'.format(18 - idade))
    print('Seu alistamento é em {}.'.format(ano+18))
else:
    print('Você deveria ter se alistado há {} ano(s).'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano+18))