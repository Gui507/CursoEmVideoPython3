def escreva(txt):
    print('-'* len(txt))
    print(txt)
    print('-' * len(txt))

from time import sleep
while True:
    escreva('\033[;42m  Sistema de Ajuda do Python  \033[m')
    c = input('Escreva o comando ou biblioteca: ').lower()
    if c == 'fim':
        break
    print(f'Acessando o manual de {c}')
    sleep(2)
    print('\033[;7m')
    help(c)
    print('\033[m')
    sleep(2)

