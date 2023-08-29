def aumentar(v = 0, p = 0, m = False):
    """
    -> Função para aumentar o preço de um produto de acordo com a porcentagem informada
    :param v: valor do produto
    :param p: porcentagem (para 10%, por exemplo, o usuário indicará o valor 10)
    :return: valor do produto aumentado em p%
    """
    n = v * (1 + p/100)
    return moeda(n) if m else n


def diminuir(v = 0, p = 0, m = False):
    """
    -> Função para diminuir o preço de um produto de acordo com a porcentagem informada
    :param v: valor do produto
    :param p: porcentagem (para 10%, por exemplo, o usuário indicará o valor 10)
    :return: valor do produto reduzido em p%
    """
    n = v * (1 - p/100)
    return moeda(n) if m else n


def dobro(v = 0, m = False):
    """
    -> Calcula o dobro do valor informado
    :param v: valor a ser informado
    :return: retorna o dobro do valor v
    """
    n = 2 * v
    return moeda(n) if m else n


def metade(v = 0, m = False):
    """
    -> Retorna metade do valor informado v
    :param v: valor informado
    :return: metade do valor informado
    """
    n = v / 2
    return moeda(n) if m else n


def moeda(v = 0, moeda = 'R$'):
    """
    -> Função que retorna o valor formatado em moeda brasileira
    :param moeda: tipo de moeda
    :param v: valor informado
    :return: valor formatado
    """
    s = f"{moeda} {v:.2f}".replace(".", ",")
    return s


