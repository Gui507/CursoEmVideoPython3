def votar(n):
    from datetime import datetime
    a = datetime.today().year
    i = a - n
    if i < 16:
        return f'Com {i} anos: VOTO NEGADO'
    elif 16 <= i < 18 or i >= 65:
        return f'Com {i} anos: VOTO OPCIONAL'
    else:
        return f'Com {i} anos: VOTO OBRIGATÓRIO'

n = int(input('Em que ano você nasceu? '))
print(votar(n))
