def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[0m')
        except KeyboardInterrupt:
            print('\033[0;31m\nO usuário preferiu não digitar esse número.\033[0m')
            return 0
        else:
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except(TypeError, ValueError):
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[0m')
        except KeyboardInterrupt:
            print('\033[0;31m\nO usuário preferiu não digitar esse número.\033[0m')
            return 0
        else:
            return valor


n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real:')
print(f'Você acabou de digitar o número inteiro {n} e o número real {r:.2f}')