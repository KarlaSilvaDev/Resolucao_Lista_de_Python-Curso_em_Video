pessoa = dict()
grupo = list()
somaIdade = médiaIdade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).strip()[0].upper()
        if pessoa['sexo'] in 'FM':
            break
        else:
            print('Resposta inválida.', end=' ')
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
        if r not in 'SN':
            print('Resposta inválida.', end=' ')
        else:
            break
    if r == 'N':
        break
média = somaIdade/len(grupo)
print('-='*30)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {média:.2f}')
print(f'- As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print(f'\n- Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] > média:
        for k, v in p.items():
            print(f'{k} = {v}', end ='; ')
    print()
print('\n<< ENCERRADO >>')