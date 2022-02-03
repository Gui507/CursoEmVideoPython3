números = []
Par = []
Impar = []
while True:
    números.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
    elif r not in 'SsNn':
        r = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip()
for i, v in enumerate(números):
    if v %2 == 0:
        Par.append(v)
    else:
        Impar.append(v)
print('='*40)
print(f'Os números digitados foram: {números}')
print(f'Pares: {Par}')
print(f'Impares: {Impar}')
