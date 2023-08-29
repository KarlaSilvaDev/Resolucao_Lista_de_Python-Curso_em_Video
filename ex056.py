"""
Exercício Python 56:
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho

e quantas mulheres têm menos de 20 anos.
"""
soma = 0
nome_mais_velho = ''
homem_mais_velho = 0
mulher_menos_20_anos = 0
for c in range(0,4):
    print('---{}ª PESSOA---'.format(c+1))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F):')).upper().strip() #Outro solução: remover o upper() e mudar a linha 18
    soma += idade
    if sexo == 'M' and idade > homem_mais_velho: #outra solução: sexo in 'Mm'
        homem_mais_velho = idade
        nome_mais_velho = nome
    elif sexo == 'F' and idade < 20: #outra solução: sexo in 'Ff'
        mulher_menos_20_anos += 1

print('Média de idade do grupo: {}'.format(soma/4))
print('Nome do homem mais velho:{}'.format(nome_mais_velho))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(mulher_menos_20_anos))