ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break
print('='*40)
print(f'{"No":<4} {"Nome":^10} {"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:^10}{a[2]:>8.1f}')
print('-'*30)
while True:
    id = int(input('Mostra nota de qual aluno? (999 interrompe) '))
    if id == 999:
        break
    if id <= len(ficha)-1:
        print(f'As notas de {ficha[id][0]} são: {ficha[id][1]}')
print('FINALIZANDO.....')
print('< VOLTE SEMPRE >')