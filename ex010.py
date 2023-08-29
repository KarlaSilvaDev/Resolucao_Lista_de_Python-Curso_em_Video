real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/4.92
euro = real/5.34
peso = real/5.49

print('Com R${:.2f}, você pode comprar: \nUS${:.2f} \n{:.2f} € \n{:.2f} CHF'.format(real, dolar, euro, peso))