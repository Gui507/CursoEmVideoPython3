from random import randint
from time import sleep
num = randint(0, 10)
chutes = 0
print('---- Jogo da Advinhação ----')
print('pensarei em um número de 0 a 10, tente advinha-lo ')
print('Pensando......')
sleep(2)
palpite = int(input('Okay, em que número eu pensei? '))
'''VALIDAÇÂO'''
while palpite != num:
    chutes += 1
    if palpite > num:
       palpite = int(input('Menos......'))
    elif palpite < num:
        palpite = int(input('Mais......'))
print(f'Depois de {chutes} tentativas, \nParabéns, você acertou')

