# Se importarmos dessa forma, só importamos a função sqrt
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num) # Nesse caso, não precisamos utilizar a referência math: math.sqrt(). A função já está na pasta
print('A raíz de {} é igual a {:.3f}.'.format(num, raiz))

"""
No caso abaixo, como importamos toda a biblioteca math, devemos informar a função a ser utilizada
chamando a referência math: math.sqrt()
import math 
num = int(input('Digite um número: '))
raiz = math.sqrt(num) 

outras funções muito utilizadas da biblioteca math:
floor = arredonda pra baixo
trunc = trunca o valor
pow = potenciação
sqrt = raiz quadrada
"""
