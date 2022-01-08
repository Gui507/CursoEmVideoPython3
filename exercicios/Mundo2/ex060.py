n = int(input('Fatorial de '))
c = n
print(f'Caclculando {n}! = ', end='')
f = 1
while c > 0:
    print(f'{c}', end='')
    print('.'if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}')
