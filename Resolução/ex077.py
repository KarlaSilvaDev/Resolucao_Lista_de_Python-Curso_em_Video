"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro', 'bcd')
for p in range(0, len(palavras)): #passa pelas palavras
    cont = 0
    print(f'\nNa palavra {palavras[p].upper()} temos ', end='')
    for l in range(0, len(palavras[p])): #passa pelas letras de cada palavra
        if (palavras[p])[l] in 'aeiou':
            print((palavras[p])[l], end=' ')
            cont += 1
    if cont == 0:
        print('zero vogal')



