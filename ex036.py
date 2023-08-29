"""
Exercício Python 36:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor = float(input(' \033[1mQual é o valor da casa? R$ \033[1m'))
salario = float(input(' \033[1mQual é o valor do salário do comprador? R$ \033[1m'))
anos =int(input(' \033[1mEm quantos anos irá pagar o empréstimo?  \033[1m'))

prestacao = valor/(12*anos)

if prestacao > salario*0.3:
    print('\033[30;41mEmpréstimo negado!\033[0m A prestação mensal seria de R${:.2f}, excedendo o valor limite de 30% do salário (R${:.2f}).'.format(prestacao, salario*0.3))
else:
    print('\033[30;42mEmpréstimo aprovado!\033[0m A parcela mensal é de R${:.2f}.'.format(prestacao))