Par = []
Impar = []
for c in range(0,7):
    n = int(input(f'Digite o {c +1}º valor: '))
    if n%2 == 0:
        Par.append(n)
    else:
        Impar.append(n)
print(f'Os valores pare digitados foram: {sorted(Par)}')
print(f'Os valores Impares digitados foram: {sorted(Impar)}')
