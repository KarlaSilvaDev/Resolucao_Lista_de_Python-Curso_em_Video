# FUNÇÕES (PARTE 2)

# INTERACTIVE HELP
#help()  # podemos digitar também diretamento no python console
#print(input.__doc__)


# DOCSTRINGS
# É basicamente uma string de documentação
def contador(i, f, p):  # parâmetros reais
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    while i <= f:
        print(f'{i}', end='..')
        i += p
    print('FIM!')


contador(2, 10, 2)  # parâmetros formais
help(contador)

# ARGUMENTOS OPCIONAIS
def somar(a, b, c = 0): #se C não for definido, receberá o valor zero (podemos definir todos como opcionais)
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)

# ESCOPO DE VARIÁVEIS


def teste():
    #global n
    # n = 3 #Se eu criar uma variável n dentro da função e não informar "global n", irão existir duas variáveis n no programa: com escopo local e global. Caso contrário, será utilizada a variável global
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2
print(f'No programa principal, n vale {n}.') # A variável n tem escopo global, variável global
teste()
#print(f'No programa principal, x vale {x}') #Dá erro porque x tem um escopo local, só funciona dentro da função teste

# RETORNO DE RESULTADOS
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
