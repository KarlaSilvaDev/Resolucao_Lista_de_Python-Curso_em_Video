"""
Exercício Python 37:
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
print('='*30)
print('Conversor de Bases Numéricas')
print('='*30)
num = int(input('Digite um número inteiro qualquer: '))
print('Escolha a base de conversão: \n[1] para binário \n[2] para octal \n[3] para hexadecimal')
base = int(input('Sua opção: '))
if base == 1:
    print('O número {} na base binária é igual a {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} na base octal é igual a {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} na base hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
    #[2:] serve para eliminar os dois primeiros caracteres (posições 0 e 1), pois estes informam apenas qual é a base
    #0b para binário, 0o para octal e 0x para hexadecimal
else:
    print('Opção inválida. Reinicie o programa.')
