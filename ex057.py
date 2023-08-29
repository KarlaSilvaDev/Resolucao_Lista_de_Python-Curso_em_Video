"""
Exercício Python 57:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Resposta inválida. Tente novamente [M/F]: ')).strip().upper()[0]
print('Resposta salva! Sexo: {}'.format(sexo))
