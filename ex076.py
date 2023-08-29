"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)
print('='*38)
print(' '*10, 'LISTAGEM DE PREÇOS', ' '*10)
print('='*38)
for c in range(0, len(produtos), 2): #Percorre a tupla de 0 ao último item de 2 em 2
    print(f'{produtos[c]:.<28}R${produtos[c+1]:>8.2f}') #Nome alinhado à esquerda em um espaço de 28 caracteteres e
    # preço à
    # direita em um espaço de 8 caracteres e com 2 casas decimais
print('-'*38)

""" Neste exemplo, utilizamos a formatação {preco:>8.2f} para exibir o preço com duas casas decimais,alinhando-o à direita em um espaço total de 8 caracteres. O valor 8 especifica o tamanho total do espaço, incluindo os dígitos e o ponto decimal. Assim, a segunda casa decimal será sempre exibida, mesmo que seja zero. """

