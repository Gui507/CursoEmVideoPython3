ranking = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
           'Fluminense', 'América - MG', 'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional',
           'São Paulo', 'Atlético Paranaense', 'Cuiaba', 'Juventude', 'Gremio', 'Bahia', 'Recife', 'Chapecoense')
print(f'A tabela atual do Campeonato Brasileiro de futebol é: {ranking}')
print(f'Os cinco primeiros colocados são: {ranking[:5]}')
print(f'Os quatro ultimos colocados são: {ranking[-4:]}')
print(f'Os times são: {sorted(ranking)}')
print(f'A Chapecoense esta na {ranking.index("Chapecoense")+1}ª posição')
