def area(l, c):
    print(f'A área de um terreno de {l}x{c}m é de {l * c}m².')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
