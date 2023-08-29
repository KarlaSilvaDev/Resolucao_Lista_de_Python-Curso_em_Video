"""
Exercício 23:
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
"""

num = int(input('Insira um número de 0 a 9999:'))
print("""Número digitado: {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(num, (num//1 % 10), (num//10 %10), (num//100 %10), (num//1000 % 10)))
