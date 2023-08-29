"""
Exercício Python 34:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%.
"""

salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    print('Seu salário com aumento de 10% é igual a R${:.2f}'.format(salario*1.1))
else:
    print('Seu salário com aumento de 15% é igual a R${:.2f}'.format(salario*1.15))
