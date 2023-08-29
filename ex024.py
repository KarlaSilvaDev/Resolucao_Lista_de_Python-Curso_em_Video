"""
Exercício 24:
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

"""

city = str(input('Insira o nome de uma cidade: ')).strip()
print(city.split()[0].upper() == 'SANTO')
