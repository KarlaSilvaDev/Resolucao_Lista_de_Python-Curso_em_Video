km = float(input('Insira a quantidade de km percorrido(s) pelo carro: '))
dias = int(input('Insira a quantidade de dia(s) pelos quais o carro foi alugado: '))
preco = 60*dias + 0.15*km
print('O valor para {:.2f}km percorridos e {} dias de aluguel é de R${:.2f}.'.format(km, dias, preco))
