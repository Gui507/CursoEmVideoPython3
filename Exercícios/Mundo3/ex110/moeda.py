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


def resumo(preço, taxaa=10, taxar=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumentando {taxaa}%: \t{aumentar(preço, taxaa, True)}')
    print(f'Reduzindo {taxar}%: \t\t{diminuir(preço, taxar, True)}')
    print('-'*40)