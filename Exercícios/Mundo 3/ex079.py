num = list()
while True:
    n = int(input('Digite um número '))
    if n not in num:
        num.append(n)
        print('valor adicionado com sucesso.....')
    else:
        print('Valor repetido, não vou registrar.')
    opcao = input('Deseja continuar? [S/N]').upper().strip()
    while opcao not in 'SN':
        opcao = input('Opção inválida. Deseja continuar? [S/N]').upper().strip()
    if opcao == 'N':
        break
print(f'os valores digitados foram\n{sorted(num)}')