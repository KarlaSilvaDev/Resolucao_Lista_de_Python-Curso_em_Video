numeros = []
for c in range(0, 5):
        num = int(input('Digite um número: '))
        if c == 0 or num > numeros[-1]: #APPEND se for o primeiro ou o último
            numeros.append(num)
            print('Adicionado ao final da lista...')
        else:
            for pos in range(0, len(numeros)):
                if num <= numeros[pos]:
                    numeros.insert(pos, num)
                    print(f'Adicionado na posição {pos} da lista...')
                    break
print(numeros)








