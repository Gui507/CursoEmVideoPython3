from random import randint
from time import sleep
computador = randint(0,10)
cont = 0
while True:
    jogador = int(input('Digite um número: '))
    opcao =' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    if opcao == 'P':
        if (computador + jogador) % 2 == 0:
            r = 'Par'
            cont += 1
            print(f'Voce jogou {jogador} e o computador {computador}, o resultado foi {r}')
            print('Voce ganhou, vamos jogar novamente')
            sleep(2)
        else:
            r = 'Impar'
            break
    elif opcao == 'I':
        if (computador + jogador) %2 == 1:
            r = 'Impar'
            cont += 1
            print(f'Voce jogou {jogador} e o computador {computador}, o resultado foi {r}')
            print('Voce ganhou, vamos jogar novamente')
        else:
            r = 'Par'
            break
print(f'Voce jogou {jogador} e o computador {computador}, o resultado foi {r}')
print('Voce perdeu')
print(f'GAME OVER! Total de vítórias seguidas: {cont}')
