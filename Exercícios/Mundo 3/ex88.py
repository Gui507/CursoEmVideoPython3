from random import randint
print('-'*40)
print('          JOGA NA SENA          ')
print('-'*40)
números = []
jogos = []
quantidade = int(input('Quantos jogos voce quer que eu sorteie? '))
tot = 1
print('-'*10, f'SORTEANDO {quantidade} JOGOS', '-'*10)
while tot <= quantidade:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in números:
            números.append(n)
            cont += 1
        if cont == 6:
            break
    números.sort()
    jogos.append(números[:])
    números.clear()
    tot += 1
for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}')