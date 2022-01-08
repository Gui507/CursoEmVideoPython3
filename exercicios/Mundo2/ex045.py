##fazendo o PC escolher
from random import choice
o = ['Pedra', 'Papel', 'Tesoura']
c = choice(o)
##escolha do jogador
j = int(input('Faça a sua escolha\n[0]Pedra\n[1]Papel\n[2]Tesoura\n'))
##interação
from time import sleep
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PÔ')
##Lógica
##Escolhendo Pedra
if c == 'Pedra' and j == 0:
    print('Computador: Pedra\nJogador: Pedra\nEMPATE')
elif c == 'Pedra' and j == 1:
    print('Computador: Pedra\nJogador: Papel\nVITÓRIA')
elif c == 'Pedra' and j == 2:
    print('Computador: Pedra\nJogador: Tesoura\nDERROTA')
##Escolhendo Papel
elif c == 'Papel' and j == 0:
    print('Computador: Papel\nJogador: Pedra\nDERROTA')
elif c == 'Papel' and j == 1:
    print('Computador: Papel\nJogador: Papel\nEMPATE')
elif c == 'Papel' and j == 2:
    print('Computador: Papel\nJogador: Tesoura\nVITÓRIA')
##Escolhendo Tesoura
elif c == 'Tesoura' and j == 0:
    print('Computador: Tesoura\nJogador: Pedra\nVITÓRIA')
elif c == 'Tesoura' and j == 1:
    print('Computador: Tesoura\nJogador: Papel\nDERROTA')
elif c == 'Tesoura' and j == 2:
    print('Computador: Tesoura\nJogador: Tesoura\nEMPATE')
else:
    print('Opção inválida')
