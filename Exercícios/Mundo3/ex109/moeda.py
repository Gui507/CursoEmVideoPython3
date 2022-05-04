def aumentar(preço=0, taxa=0, formatado=False):
    res = preço + (taxa/100 * preço)
    return res if not formatado else moeda(res)


def diminuir(preço=0, taxa=0, formatado=False):
    res = preço - (taxa/100 * preço)
    return res if not formatado else moeda(res)


def dobro(preço=0, formatado=False):
    res = 2 * preço
    return res if not formatado else moeda(res)


def metade(preço=0, formatado=False):
    res = preço * 1/2
    return res if not formatado else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')