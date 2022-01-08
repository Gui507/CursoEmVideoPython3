s = 0
r = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        r += 1
        s += c
print(f'A soma de todos os {r} valores encontrados é igual a {s} ')
