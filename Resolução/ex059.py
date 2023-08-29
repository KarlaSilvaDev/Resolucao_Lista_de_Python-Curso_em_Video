from time import sleep
nums = []
#ENTRADA
for c in range(0,2):
    nums.append(float(input('{}º valor: '.format(c+1))))
option = 0
while option != 5: # VALIDAÇÃO
    # MENU
    print('\033[1;30;42m MENU \033[m')
    print('[1] somar \n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    option = int(input('Escolha uma das opções acima: '))
    while 1 > option > 5:
        print('Opção inválida! Tente novamente')
    # OPERAÇÕES
    if option == 1:
        print('\033[47;30m {} + {} = {}\033[m'.format(nums[0], nums[1], nums[0] + nums[1]))
    elif option == 2:
        print('\033[47;30m{} x {} = {}\033[m'.format(nums[0], nums[1], nums[0] * nums[1]))
    elif option == 3:
        if (nums[0] > nums[1]):
            print('\033[47;30mEntre {} e {}, o maior número é: {}\033[m'.format(nums[0], nums[1], nums[0]))
        else:
            print('\033[47;30mEntre {} e {}, o maior número é: {}\033[m''.format(nums[0], nums[1], nums[1]))
    elif option == 4:
        print('---ESCOLHA NOVOS NÚMEROS---')
        for c in range(0, 2):
            nums[c] = (float(input('{}º valor: '.format(c + 1))))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('-=-'*10)
    sleep(2)
print('FIM')






