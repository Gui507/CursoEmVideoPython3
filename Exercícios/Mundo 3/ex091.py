
# ordeanar do maior para o menos
# Mostrar o ranking
from random import randint
from time import sleep
from operator import itemgetter
Jogador = {1:0, 2:0, 3:0, 4:0}
for k, v in Jogador.items():
    v = int(randint(1, 6))
    if v not in Jogador.items():
        Jogador[k]= v
        sleep(1)
    print(f'Jogador {k}: {v}')
ranking = sorted(Jogador.items(), key=itemgetter(1), reverse=True)
print('   === Ranking ===   ')
for i, j in enumerate(ranking):
    print(f'{i+1}° Lugar: Jogador {j[0]} com {j[1]}')
    sleep(1)