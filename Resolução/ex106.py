from time import sleep
cores = {'semCor':'\033[m',
         'vermelho': '\033[0;30;41m',
         'verde': '\033[0;30;42m',
         'amarelo': '\033[0;30;43m',
         'azul': '\033[0;30;44m',
         'roxo': '\033[0;30;45m',
         'branco': '\033[7m'
         }

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', cores['azul'])
    print(cores['branco'], end='')
    help(com)
    print(cores['semCor'], end='')
    sleep(2)

def titulo(msg, cor = cores['semCor']):
    tam = len(msg) + 4
    print(cor, end='')
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~'*tam)
    print(cores['semCor'], end='')
    sleep(1)

#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP!', cores['verde'])
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', cores['vermelho'])