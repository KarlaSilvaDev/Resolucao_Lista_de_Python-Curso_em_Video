"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
para viagens mais longas.
"""

dist = float(input('Qual é a distância da viagem em km? '))
if dist <= 200:
    valor = dist*0.50
    print('Para a viagem de {:.2f}km, o valor é R${:.2f}.'.format(dist, valor))
else:
    valor = dist*0.45
    print('Para a viagem de {:.2f}km, o valor é R${:.2f}.'.format(dist, valor))