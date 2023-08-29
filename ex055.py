maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior peso: {:.2f}kg | Menor peso: {:.2f}kg'.format(maior, menor))