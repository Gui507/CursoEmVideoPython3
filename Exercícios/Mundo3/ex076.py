produtos = ('Caderno', 10, 'Caneta', 2, 'Lápis', 1.50, 'Borracha', 1)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for p in range(0, len(produtos)):
    if p %2 == 0:
        print(f'{produtos[p]:.<40}', end='')
    else:
        print(f'R${produtos[p]:>6.2f}')
print('-' * 40)