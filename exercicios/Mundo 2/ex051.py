n = int(input('Digite o primeiro termo da P.A '))
r = int(input('Digite a razão dessa P.A '))
d = n + (10-1) * r
for c in range(n, d+r, r):
    print(c , end=' → ')
print('ACABOU')
