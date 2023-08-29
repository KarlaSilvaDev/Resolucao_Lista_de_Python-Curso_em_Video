"""
Exercício 22:
Crie um programa que leia o nome completo de uma pessoa  e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaço)
- Quantas letras tem o primeiro nome

"""

name = str(input('Digite o seu nome completo:')).strip() #elimina os espaços no ínicio e no fim
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minúsculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(''.join(name.split()))))
#outra forma de fazer abaixo:
print('Seu nome tem ao todo {} letras.'.format(len(name)-name.count(' ')))

"""
name.split() cria uma lista em que cada palavra da string é um elemento
''.join() junta os elementos da lista (as palavras) sem espaço, pois entra as aspas simples não há nada
Por fim, a função len() diz o tamanho da string agora sem espaços
"""
print('Seu primeiro nome é {} e tem {} letras.'.format(name.split()[0], len(name.split()[0])))
#outra forma de fazer abaixo:
print('Seu primeiro nome tem {} letras.'.format(name.find(' ')))

"""
name.split() cria uma lista em que cada palavra da string é um elemento 
[0] indica que queremos trabalhar apenas com a palavra que ocupa o índice zero da lista
Neste caso, essa palavra é o primeiro nome
Por fim, len() diz o tamanho do primeiro nome 
"""
