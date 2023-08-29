def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: o número a ser calculado
    :param show: mostrar ou não a conta
    :return: o valor do fatorial de um número num
    """
    print('-' * 20)
    f = 1
    for num in range(num, 0, -1):
        if show:
            print(f'{num} x ' if num != 1 else f'{num} = ', end='')
        f *= num
    return f


print(fatorial(5, True))
help(fatorial)
