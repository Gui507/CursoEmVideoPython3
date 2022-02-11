galera = []
pessoas = []
p = P = 0
while True:
    pessoas.append(input('Nome: '))
    pessoas.append(input('Peso: kg '))
    if len(galera) == 0:
        p = P = pessoas[1]
    else:
        if pessoas[1] < p:
            p = pessoas[1]
        if pessoas[1] > P:
            P = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    opção = input('Deseja continuar? [S/N]').strip()
    if opção in 'Nn':
        break
    elif opção not in 'SsNn':
        opção = input('Opção inválida. Deseja continuar? [S/N]').strip()
print('-'*40)
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O menor peso foi {p}kg de: ', end='')
for i in galera:
    if i[1] == p:
        print(f'{i[0]}, ', end='')
print(f'\nO maior peso foi {P}kg de: ', end='')
for i in galera:
    if i[1] == P:
        print(f'{i[0]}, ', end='')
