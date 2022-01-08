#CABEÇALHO
print('='*40)
print('{:^40}'.format('CAIXA RÁPIDO'))
print('='*40)
#VARIÁVEIS
c50 = c20 = c10 = c01 = 0
#INÍCIO
valor = int(input('Qual é o valor a ser sacado? R$'))
#LÓGICA
while valor > 0:
    if valor >= 50:
        c50 += 1
        valor -= 50
    elif valor >= 20:
        c20 += 1
        valor -= 20
    elif valor >= 10:
        c10 += 1
        valor -= 10
    elif valor >= 1:
        c01 += 1
        valor -= 1
#FINAL
print(f'Total de {c50} cédulas de R$50')
print(f'Total de {c20} cédulas de R$20')
print(f'Total de {c10} cédulas de R$10')
print(f'Total de {c01} cédulas de R$1')
