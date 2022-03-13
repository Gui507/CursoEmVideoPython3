# mostrar os resultados
from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('CTPS (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contrtação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - nascimento
print('='*40)
for k, v in dados.items():
    print(f'{k}: {v}')
