"""
Exercício Python 65:
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
soma = cont = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    resp = str(input('Você deseja continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Resposta inválida! Deseja continuar? [S/N] ')).strip()[0]

print('\033[1;30;42m RESULTADO \033[m')
print('Quantidade de valores lidos: {}'.format(cont))
print('Média: {}'.format(soma/cont))
print('Maior valor: {}'.format(maior))
print('Menor valor: {}'.format(menor))

