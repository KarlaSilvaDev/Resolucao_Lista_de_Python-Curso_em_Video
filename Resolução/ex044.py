"""
Exercício Python 44:
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""


preco = float(input('Qual o valor do produto? R$'))

print("""Escolha a forma de pagamento: 
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão""")
pagamento = int(input('Forma escolhida: '))

if pagamento == 1:
    print('Preço normal: R${:.2f}\nForma de pagamento: à vista dinheiro/cheque\nDesconto: 10% \nValor a ser pago: R${:.2f}'.format(preco, preco*0.9))
elif pagamento == 2:
    print('Preço normal: R${:.2f}\nForma de pagamento: à vista no cartão\nDesconto: 5%\nValor a ser pago: R${:.2f}'.format(preco, preco*0.95))
elif pagamento == 3:
    print('Preço normal: R${:.2f}\nForma de pagamento: em até 2x no cartão\nDesconto: Não aplicável\nValor a ser pago: R${:.2f}'.format(preco, preco))
elif pagamento == 4:
    print('Preço normal: R${:.2f}\nForma de pagamento: em 3x ou mais no cartão\nJuros: 20%\nValor a ser pago: R${:.2f}'.format(preco, preco*1.2))
else:
    print('Forma de pagamento inválida. Reinicie o programa.')
