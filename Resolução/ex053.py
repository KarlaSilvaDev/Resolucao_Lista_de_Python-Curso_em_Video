"""
Exercício Python 53:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.
"""
print('='*40)
print('Verificando se a frase é um PALÍNDROMO:')
print('='*40)
frase = str(input('Digite a frase a ser analisada: ')).strip().upper()
frase = ''.join(frase.split())
inicio = len(frase) - 1
list = []
for c in range(inicio, -1, -1):
    list = list + [frase[c]]
invertida = ''.join(list)

# esse for pode ser substituído por invertida = frase[::-1]
if invertida == frase:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase não é um PALÍNDROMO!')




