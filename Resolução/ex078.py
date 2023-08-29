num = []
for c in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))

print(f'Você digitou os valores {num}')
print(f'O maior valor é {max(num)} nas posições ', end='')
for c, v in enumerate(num):
    if v == max(num):
        print(f'{c}...', end='')
print(f'\nO menor valor é {min(num)} nas posições ', end='')
for c, v in enumerate(num):
    if v == min(num):
        print(f'{c}...', end='')