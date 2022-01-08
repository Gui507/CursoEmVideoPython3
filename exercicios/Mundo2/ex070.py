#CABEÇALHO
print('-'*40)
print('{:^40}'.format('ALINE FRALDAS ATACADO'))
print('-'*40)
#VARIÁVEIS
total = mais1000 = pbarato = cont = 0
nbarato = str('')
#LÓGICA
while True:
    nome = str(input('Nome do Produto: ')).capitalize()
    preco = float(input('Preço do produto: R$'))
    total += preco
    cont += 1
    #MAIS BARATO
    if cont == 1 or preco < pbarato:
        pbarato = preco
        nbarato = nome
    opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while opcao not in 'SN': #VALIDAÇÃO
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    #ANÁLISE
    if preco > 1000:
        mais1000 += 1
   #INTERROMPE
    if opcao == 'N':
        break
#RESULTADO
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000')
print(f'O produto mais barato foi {nbarato} custando R${pbarato:.2f}')
