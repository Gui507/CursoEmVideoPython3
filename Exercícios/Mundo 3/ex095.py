dados = {}
gols = list()
time = []
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ')).capitalize()
    dados['Partidas'] = int(input('Quantas partidas ele jogou? '))
    gols.clear()
    for c in range(0, dados['Partidas']):
        gols.append(int(input(f'Gols na partida {c + 1}: ')))
    dados['gols'] = gols[:]
    dados['Total'] = sum(gols)
    time.append(dados.copy())
    while True:
        r = str(input('Deseja continuar? [S/N]')).upper()[0]
        if r in 'SN':
            break
        else:
            print('Opção inválida. Tente novamente.')
    if r == 'N':
        break
print('='*80)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
print('-'*80)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*80)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    elif busca >= len(time):
        print('Jogador inexistente')
    else:
        print(f"LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f'{g} gols na partida {i+1}')
print('Programa encerrado. Obrigado por usar.')
