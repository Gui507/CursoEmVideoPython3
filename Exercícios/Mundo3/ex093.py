dados = {}
gols = []
dados['Nome'] = str(input('Nome: '))
dados['Partidas'] = int(input('Quantas partidas ele jogou? '))
for c in range(0, dados['Partidas']):
    dados['gols'] = gols
    gols.append(int(input(f'Gols na partida {c + 1}: ')))
    dados['Total'] = sum(gols)
print('='*80)
print(dados)
print('='*80)
for k, v in dados.items():
    print(f'{k}: {v}')
print('='*80)
print(f"O jogador {dados['Nome']} jogou {dados['Partidas']} partidas ")
for i, c in enumerate(gols):
        print(f'    Na partida {i + 1} fez {c} gols')
print(f"foi um total de {dados['Total']} gols")
