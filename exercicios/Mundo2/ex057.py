sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção inválida, tente novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
