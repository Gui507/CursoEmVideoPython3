n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
m = (n1 + n2)/2
if m < 5.0:
    print(f'sua media foi {m}, você foi REPROVADO')
elif 5.0 <= m <= 6.9:
    print(f'Suam média foi {m}, você está de RECPERAÇÂO')
elif m >= 7:
    print(f'Sua média foi {m}, Parabéns! você foi APROVADO')
