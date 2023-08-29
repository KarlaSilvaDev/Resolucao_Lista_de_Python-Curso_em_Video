num = []
while True:
    num.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
        if resp in 'SN':
            break
        else:
            print('Resposta inválida. ', end='')
    if resp == 'N':
        break
pares = []
impares = []
for valor in num:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')