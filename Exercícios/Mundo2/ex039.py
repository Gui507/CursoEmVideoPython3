from datetime import date
a = date.today().year
n = int(input('Em que ano você nasceu? '))
i = a - n
if i == 18:
    print('Aliste-se, o dever te chama')
elif i > 18:
    print(f'voce esta atrassado {i - 18} ano(s). Aliste-se, o dever te chama.')
elif i <  18:
    print(f'Seu alistamento será daqui a {18 - i} ano(s)')