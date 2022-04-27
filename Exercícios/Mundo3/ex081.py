lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
    elif r not in 'SsNn':
        r = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip()
print('=-'*30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}.')
print('O valor 5 está na lista'if 5 in lista else 'O valor 5 não foi encontrado na lista')
