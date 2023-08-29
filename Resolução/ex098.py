from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim: #contagem crescente
        while inicio <= fim:
            print(inicio, end=' ')
            inicio += passo
            sleep(0.5)
        print('FIM!')
    else: #contagem decrescente
        while inicio >= fim:
            print(inicio, end=' ')
            inicio -= passo
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
