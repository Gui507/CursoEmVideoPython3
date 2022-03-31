pessoa = {}
lista = mulheres = imaior = []
soma = media = 0
while True:
    pessoa['Nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in "MF":
            break
        print('Opção inválida, tente novamente. Digite M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    lista.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if r in 'SN':
            break
        print('Opção inválida, tente novamente. Digite S ou N')
    if r == 'N':
        break
print('='*40)
print(f'Foram cadastradas {len(lista)} pessoas')
media = soma / len(lista)
print(f'A média de idade é {media}')
print('As mulheres cadastradas foram:', end=' ')
for p in lista:
    if p['Sexo'] == 'F':
        print(p['Nome'], end=', ')
print()
print('As pessoas com idade acima da media são:')
for p in lista:
    if p['Idade'] >= media:
        print(f"    * {p['Nome']} com {p['Idade']} anos")
print('<<PROGRAMA ENCERRADO>>')