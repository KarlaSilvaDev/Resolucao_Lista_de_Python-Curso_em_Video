"""
Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

from datetime import date
print('-=-'*12)
print('Confederação Nacional de Natação')
print('-=-'*12)
ano = int(input('Insira o ano de nascimento do atleta com 4 caracteres: '))
idade = date.today().year - ano

if idade <= 9:
    print('Idade: {} | Categoria: MIRIM'.format(idade))
elif idade <= 14:
    print('Idade: {} | Categoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('Idade: {} | Categoria: JUNIOR'.format(idade))
elif idade <= 20:
    print('Idade: {} | Categoria: SÊNIOR'.format(idade))
else:
    print('Idade: {} | Categoria: MASTER'.format(idade))

