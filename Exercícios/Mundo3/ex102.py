def fatorial(n, show=False):
    '''
    → Calcula o fatorial de um número
    :param n: número a ser calculado
    :param show: mostra o calculo
    :return: fatorial de n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


print(fatorial(10, show=True))
