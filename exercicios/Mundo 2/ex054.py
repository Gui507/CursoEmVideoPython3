from datetime import date
y = date.today().year
m = 0
k = 0
for c in range(1, 8):
    n = int(input(f'Ano de nascimento da {c}° pessoa: '))
    a = y - n
    if a < 18:
        k += 1
    elif a >= 18:
        m += 1
print(f'Existem {m} maiores e {k} menores')
