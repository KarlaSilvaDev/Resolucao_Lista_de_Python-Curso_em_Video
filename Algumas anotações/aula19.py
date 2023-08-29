# DICIONÁRIOS
"""Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
"""

print('\nDECLARANDO UM DICIONÁRIO')
pessoas = {'nome': 'Karla', 'sexo': 'F', 'idade': 29}
print(pessoas)
#print(pessoas[0]) #Nesse caso, será apresentado um erro, pois não existe mais o índice 0
print(pessoas['nome'])

print('\nCHAVES, VALORES E ITEMS')
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('\nACESSANDO DICIONÁRIOS ATRAVÉS DE LAÇOS')
print('CHAVES:')
for k in pessoas.keys():
    print(k, end='...')
print('\nVALORES:')
for v in pessoas.values():
    print(v, end='...')
print('\nITENS: ')
for k, v in pessoas.items(): #Equivale ao enumerate das tuplas e listas
    print(f'{k} = {v}')

print('\nAPAGANDO DADOS DO DICIONÁRIO')
del pessoas['sexo'] #DELETANDO UM ITEM
pessoas['nome'] = 'Andréa'  #MUDANDO O VALOR DE UM ITEM
pessoas['peso'] = 62.2 #ADICIONANDO UMA CHAVE E SEU RESPECTIVO VALOR (NÃO PRECISA DE APPEND)
print(pessoas)

print('\nCRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA')
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])

print('\n CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA ATRAVÉS DO INPUT')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #Não dá pra usar estado[:], pois estado é  um dicionário
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end = ' ')
    print()
