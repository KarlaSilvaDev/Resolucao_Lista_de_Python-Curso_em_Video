# LISTAS COMPOSTAS
teste = list()
teste.append('Karla')
teste.append(29)
galera = list()
#galera.append(teste) - Isso cria uma ligação entre as estruturas
galera.append(teste[:]) #Isso cria uma cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#ACESSANDO OS DADOS DENTRO DA LISTA
grupo = [['Karla', 29], ['Ysa', 28], ['Andréa', 55], ['Sérgio', 61]]
print(grupo[0][0]) #Karla
print(grupo[2][1]) #55
print(grupo[3]) # ['Sergio', 61]

for p in grupo:
    print(f'{p[0]} tem {p[1]} anos de idade.')

# ENTRADA DE DADOS:
alunos = list()
dados = list()
totmaior = totmenor = 0
for cont in range(0, 3):
    dados.append(str(input('Nome: ').strip().title()))
    dados.append(int(input('Idade: ')))
    alunos.append(dados[:])
    dados.clear()
print(alunos)

for p in alunos:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')