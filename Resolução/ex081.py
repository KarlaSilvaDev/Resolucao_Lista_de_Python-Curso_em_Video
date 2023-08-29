numeros = []
cont = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    cont += 1
    resp = ''
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
        if resp not in 'SN':
            print('Resposta Inválida. ', end='')
        else:
            break
    if resp == 'N':
        break
print('-='*30)
print(f'Foram digitados {cont} números.')
print(f'A lista ordenada de forma decrescente: {sorted(numeros, reverse= True)}')
print("O valor 5 está na lista" if (5 in numeros)else "O valor 5 não está na lista")
