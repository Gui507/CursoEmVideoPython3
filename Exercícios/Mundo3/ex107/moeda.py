def aumentar(preço, taxa):
    res = preço + (taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (taxa/100)
    return res


def dobro(preço):
    res = 2 * preço
    return res


def metade(preço):
    res = preço * 1/2
    return res