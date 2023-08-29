matriz = [[], [], []]
somaPares = soma3Col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        if c == 2:
            soma3Col += matriz[l][c]
    print()
print('='*30)  
print(f'\nSoma de todos os valores pares digitados: {somaPares}')
print(f'Soma dos valores da terceira coluna: {soma3Col}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')
