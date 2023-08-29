from time import sleep
def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}. ' if len(num) !=0 else '')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

