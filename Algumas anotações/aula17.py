# LISTAS (MUTÁVEIS)
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim'] #entre colchetes
print(lanche)
lanche [3] = 'Picolé'  #Como são mutáveis, as listas aceitam esse comando
print(lanche)

# ADICIONANDO NOVAS POSIÇÕES NA LISTA
#No final da lista
lanche.append('Cookie')
print(lanche)
#Entre dois elementos já existente na lista
lanche.insert(1, 'Cachorro Quente') #Insere o item na posição 1, jogando para a posição c+1 todos os elementos com
# índice igual ou superior
print(lanche)

#ELIMINANDO ITENS
del lanche[3] #elimina o item na posição 3
print(lanche)
lanche.pop(3) #normalmente, é utilizado para eliminar o último elemento, mas podemos passar a posição do elemento
# também
print(lanche)
lanche.remove('Suco') #elimina o item de acordo com o valor e não com a posição. Essa função só remove a primeira
# ocorrência do valor procurado
print(lanche)
lanche.pop() #elimina o último elemento
print(lanche)

# PARA MOSTRAR OS VALORES NA TELA SERVEM OS MESMAS DICAS DA AULA 16 DE TUPLAS

#ATENÇÃO: A PARTIR DO MOMENTO QUE IGUALAMOS LISTAS, O PYTHON CRIA UMA LIGAÇÃO ENTRE ELAS
a = [2, 3, 4, 7]
b = a
c = a[:]  #Assim, o python não cria a ligação entre as listas
b[2] = 8
print(f'Lista A: {a}') #O python mudou a lista A também, pois foram ligadas
print(f'Lista B: {b}')
print(f'Lista C: {c}')



#DECLARANDO LISTA ATRAVÉS DA FUNÇÃO LIST E OUTRAS FUNÇÕES DE MANIPULAÇÃO
valores = list(range(4, 11)) #cria uma lista valores = [4, 5, 6, 7, 8, 9, 10]
valores.sort() #ordena os valores
valores.sort(reverse=True) #ordena na ordem reversa
len(valores) #tamanho da lista

