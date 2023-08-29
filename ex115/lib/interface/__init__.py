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


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lst):
    cabeçalho('MENU PRINCIPAL')
    for k, v in enumerate(lst):
        print(f'\033[0;33m{k+1} - \033[0;34m{v}\033[m')
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc

