n = int(input('Digite o primeiro termo da P.A '))
r = int(input('Digite a razão dessa P.A '))
c = 10
while c != 0:
    print(n, end=' → ')
    n += r
    c -=1
print('ACABOU')
