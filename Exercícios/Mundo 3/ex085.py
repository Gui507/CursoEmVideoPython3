núm = [[], []]
for c in range(1,8):
    n = int(input(f'Digite o {c}º valor: '))
    if n%2 == 0:
        núm[0].append(n)
    else:
        núm[1].append(n)
print(f'Os valores pare digitados foram: {sorted(núm[0])}')
print(f'Os valores Impares digitados foram: {sorted(núm[1])}')
