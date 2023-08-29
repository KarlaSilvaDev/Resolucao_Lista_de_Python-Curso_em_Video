"""
Exercício Python 48:
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que
se encontram no intervalo de 1 até 500.
"""
soma = 0
for c in range (1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print('A soma dos números ímpares entre 1 e 500 é igual a {}'.format(soma))
# Outra forma
"""
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma dos números ímpares entre 1 e 500 é igual a {}'.format(soma))
"""