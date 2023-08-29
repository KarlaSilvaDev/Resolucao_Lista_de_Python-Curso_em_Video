pessoas = list()
pessoa = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ').strip().title()))
    pessoa.append(float(input('Peso (kg): ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if maior < pessoa[1]:
            maior = pessoa[1]
        if menor > pessoa[1]:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
        if r in 'SN':
            break
        else:
            print('Resposta inválida! ', end = '')
    if r == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {menor}kg. Peso de ', end ='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')