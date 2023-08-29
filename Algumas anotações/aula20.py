print("""FUNÇÕES
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.""")


def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


def soma(a, b):
    print(f'{a} + {b} = {a+b}')


#EMPACOTAMENTO
def contador(*num): #cria uma tupla
    print(len(num))


def dobra(lst):
    pos = 0
    while pos < (len(lst)):
        lst[pos] *= 2
        pos += 1



mensagem('     SISTEMA DE ALUNOS     ')
soma(5, 4)
soma(b=2, a=1)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0, 2] 
dobra(valores)
print(valores)