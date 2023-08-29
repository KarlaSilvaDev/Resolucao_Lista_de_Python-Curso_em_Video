print('-=-'*8)
print('Cálculo do IMC')
print('-=-'*8)
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso/pow(altura,2)

if imc < 18.5:
    print('\033[30;41mIMC: {:.1f} | Situação: ABAIXO DO PESO\033[0m'.format(imc))
elif 18.5 <= imc < 25:
    print('\033[30;42mIMC: {:.1f} | Situação: PESO IDEAL\033[0m'.format(imc))
elif 25 <= imc < 30:
    print('\033[30;43mIMC: {:.1f} | Situação: SOBREPESO\033[0m'.format(imc))
elif 30 <= imc < 40:
    print('\033[30;41mIMC: {:.1f} | Situação: OBESIDADE\033[0m'.format(imc))
else:
    print('\033[30;41mIMC: {:.1f} | Situação:OBESIDADE MÓRBIDA\033[0m'.format(imc))
