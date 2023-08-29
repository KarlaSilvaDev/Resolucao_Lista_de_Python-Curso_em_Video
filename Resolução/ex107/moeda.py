def aumentar(v, p):
    """
    -> Função para aumentar o preço de um produto de acordo com a porcentagem informada
    :param v: valor do produto
    :param p: porcentagem (para 10%, por exemplo, o usuário indicará o valor 10)
    :return: valor do produto aumentado em p%
    """
    n = v * (1 + p/100)
    return n


def diminuir(v, p):
    """
    -> Função para diminuir o preço de um produto de acordo com a porcentagem informada
    :param v: valor do produto
    :param p: porcentagem (para 10%, por exemplo, o usuário indicará o valor 10)
    :return: valor do produto reduzido em p%
    """
    n = v * (1 - p/100)
    return n


def dobro(v):
    """
    -> Calcula o dobro do valor informado
    :param v: valor a ser informado
    :return: retorna o dobro do valor v
    """
    n = 2 * v
    return n


def metade(v):
    """
    -> Retorna metade do valor informado v
    :param v: valor informado
    :return: metade do valor informado
    """
    n = v / 2
    return n

