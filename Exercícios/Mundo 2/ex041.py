from datetime import date
a = int(input('Qual o ano de nascimento? '))
y = date.today().year
i = y - a
if i <= 9:
    print(f'O aluno tem {i} anos e se encaixa na categoria Mirim.')
elif 9 < i <= 14:
    print(f'O aluno tem {i} anos e se encaixa na categoria Infantil.')
elif 14 < i <= 19:
    print(f'O aluno tem {i} anos e se encaixa na categoria Junior.')
elif 19 < i <= 20:
    print(f'O aluno tem {i} anos e se encaixa na categoria Sênior.')
else:
    print(f'O aluno tem {i} anos e se encaixa na categoria Master.')
