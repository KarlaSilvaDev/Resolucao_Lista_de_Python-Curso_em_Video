"""
Exercício Python 038:
Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:
– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""
print('-=-'*10)
print('Comparando dois números inteiros')
print('-=-'*10)
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor, igual a {}, é maior.'.format(n1))
elif n2 > n1:
    print('O segundo valor, igual a {}, é maior.'.format(n2))
else:
    print('Não existe valor maior. Os dois são iguais!')
