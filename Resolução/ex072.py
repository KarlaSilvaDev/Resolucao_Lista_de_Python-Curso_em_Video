""" Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""
# TUPLA
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
# ENTRADA E VALIDAÇÃO
while True:
    num = int(input('Entre com um número inteiro entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {extenso[num]}.')
        while True:
            resp = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
            if resp in 'SN':
                break
            else:
                print('Resposta inválida!', end=' ')
        if resp == 'N':
            break
    else:
        print('Resposta inválida!', end =' ')

print('PROGRAMA ENCERRADO!')



