from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números gerados foram {numeros}')
print(f'O maior número foi {max(numeros)}')
print(f'O menor número foi {min(numeros)}')
