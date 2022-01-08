## Coleta de Dados
c = float(input('Qual é o valor da casa? R$ '))
s = float(input('Qual é o seu salário? R$ '))
a = int(input('Em quantos anos você planeja quitar essa casa?'))
print('Analisando...')
from time import sleep
sleep(4)
## Analise de Dados
p = c/(a * 12)
r = 0.3 * s
if p > r:
    print('Empréstimo Negado.')
else:
    print('Emprétimo Aprovado.')