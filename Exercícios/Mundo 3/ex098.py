def contador(i, f, p):
    from time import sleep
    print("-"*40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    c = i
    if i < f:
        while c <= f:
            print(f'{c} ', end='')
            sleep(0.25)
            if p == 0:
                p = 1
                c += p
            else:
                c += p
    elif i > f or p < 0:
        while c >= f:
            print(f'{c} ', end='')
            sleep(0.25)
            if p == 0:
                p = 1
                c -= p
            else:
                c -= p

    print()
    print("-"*40)

contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem Personalizada')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo:')))