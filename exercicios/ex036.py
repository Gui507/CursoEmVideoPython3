from time import sleep
c = float(input('Qual é o valor da casa? R$'))
s = float(input('Qual é o seu salário? R$'))
a = int(input('Em quantos anos você pretende quitar essa casa?'))
p = c/(a*12)
r = 0.30*s
print('Analisando....')
sleep(10)
if r < p:
    print('Empréstimo \033[0;31;1mNEGADO!\033[0m')
else:
    print('Empréstimo \033[0;32;1mAPROVADO!\033[0m')
