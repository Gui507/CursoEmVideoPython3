#CABEÇALHO
print('-'*40)
print('{:^40}'.format('CADASTRO DE PESSOA'))
print('-'*40)
#VaARIÁVEIS
maior = 0
homem = 0
wmenor20 = 0
#LÓGICA
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': #VALIDAÇÃO
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 40)
    opcao = ' '
    while opcao not in 'SN': #VALIDAÇÃO
         opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    print('-' * 40)
    #ANÁLISE
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        wmenor20 += 1
    #INTERROMPE
    if opcao == 'N':
        break
#RESULTADO
print(f'''Total de pessoas com mais de 18 anos: {maior}
Ao todo {homem} homens cadastrados
E temos {wmenor20} mulheres com menos de 20 anos:''')
