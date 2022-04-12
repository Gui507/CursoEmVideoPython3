def escreva(txt):
    print('-'* (len(txt)+2))
    print(txt)
    print('-' * (len(txt)+2))

from time import sleep
while True:
    escreva('\033[;42mSistema de Ajuda do Pytho\033[m')
    c = input('Escreva o comando ou biblioteca: ').lower()
    if c == 'fim':
        break
    print(f'Acessando o manual de {c}')
    sleep(2)
    print('\033[;7m')
    help(c)
    print('\033[m')
    sleep(2)

