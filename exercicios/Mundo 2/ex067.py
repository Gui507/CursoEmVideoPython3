print('-'*40)
print('{:^40}'.format('TABUADA'))
print('-'*40)
while True:
    n = int(input('Digite um numero para ver sua tabuada [Valor negativo para]: '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n}  X {c:2} = {n*c}')
    print('-'*40)
