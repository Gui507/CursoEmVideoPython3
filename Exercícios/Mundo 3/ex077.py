palavras = ('aprender', 'ensinar', 'porgramar', 'desenvolver', 'python')
for p in palavras:
    print(f'\nNa palavra {p.capitalize()} temos as vogais: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l,end=' ')
