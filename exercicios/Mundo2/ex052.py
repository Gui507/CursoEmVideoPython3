n = int(input('Digite um número '))
d = 0
for c in range(1,n+1):
  if n % c == 0:
     print('\033[m', end=' ')
     d += 1
  else:
    print('\033[31m', end=' ')
print(f'\n\033[m o numero {n} foi dividido {d} vezes')
if d == 2:
  print('e por isso ele é primo')
else:
  print('E por isso ele não é primo')