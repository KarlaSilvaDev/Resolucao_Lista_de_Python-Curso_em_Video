"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

nums = (int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')))
print(f'Você digitou os valores {nums}')
cont = pares = 0
for n in nums:
    if n == 9:
        cont +=1
print(f'O valor 9 apareceu {cont} vez(es)' if cont >=1 else 'O valor 9 não foi digitado em nenhuma posição')

if 3 in nums:
    print(f'O primeiro valor três está na {nums.index(3)+1}ª posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

cont = 0

for n in nums:
    if n % 2 == 0:
        cont += 1
if cont >= 1:
    print('Os números pares foram: ', end='')
    for n in nums:
        if n % 2 == 0:
            print(n, end=' ')
else:
    print('Não foram digitados números pares.')





