"""
Exercício Python 70:
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
print('-'*30)
print('     LOJA SUPER BARATÃO     ')
print('-'*30)
total = maisMil = maisBarato = cont = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    if cont == 0:
        maisBarato = preco
        nomeMaisBarato = nome
    else:
        if preco < maisBarato:
            maisBarato = preco
            nomeMaisBarato = nome
    cont += 1
    total += preco
    if preco > 1000:
        maisMil += 1
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
        if resp in 'SN':
            break
        else:
            print('Resposta Inválida!')
    if resp == 'N':
        break
print('-'*20,' FIM DO PROGRAMA ','-'*20)
print('Total gasto na compra: R${:.2f}'.format(total))
print('Quantidade de produtos que custam mais de R$1000,00: {}'.format(maisMil))
print('Nome do produto mais barato: {} (R${:.2f})'.format(nomeMaisBarato, maisBarato))