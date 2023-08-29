numeros = [[], []]
dados = list()
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
    dados.clear()
print(f'Valores pares digitados: {sorted(numeros[0])}')
print(f'Valores ímpares digitados: {sorted(numeros[1])}')