def leiaInt(str):
    while True:
        valor = input(str)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[0m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
