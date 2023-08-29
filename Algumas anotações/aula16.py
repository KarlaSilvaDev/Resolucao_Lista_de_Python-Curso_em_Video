# TUPLA(IMUTÁVEIS)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #Pode ser criada sem parênteses
pessoa = ('Karla', 29, 62.2) #Podemos misturar tipos de dados dentro das tuplas
del(pessoa) #Único comando capaz de modificar uma tupla, deletando-a COMPLETAMENTE durante a execução do programa.

# FATIAMENTO
print(lanche[1]) #Na hora de referenciar, sempre usamos colchetes
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
#lanche[1] = 'milkshake'  Não pode ser usado, pois tuplas são imutáveis

# FORMAS DE EXIBIR OS ITENS DE UMA TUPLA
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# ORGANIZAR
print(sorted(lanche)) #No caso de strings, mostra em ordem alfabética. Não muda a ordem na tupla, apenas na exibição.

# "SOMA" DE TUPLAS
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #Exibe (2, 5, 4, 5, 8, 1, 2)

#OPERAÇÕES COM ELEMENTOS DENTRO DA TUPLA
print(c.count(5)) #Exibe 2
print(len(c)) #Exibe 7
print(c.index(8)) #Exibe a posição (índice) do número 8 na tupla
print(c.index(5,2)) #Exibe a posição do número 5 na tupla, começando a analisar da posição 1 em diante

