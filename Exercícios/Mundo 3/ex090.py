aluno = {'Nome':'','Média':'','Situação':''}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Média'] >= 7.0:
    aluno['Situação'] = str('Aprovado')
else:
    aluno['Situação'] = str('Reprovado')
for k, v in aluno.items():
    print(f'{k}: {v}')

