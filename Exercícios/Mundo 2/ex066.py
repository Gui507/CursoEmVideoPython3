cont = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma entre os {cont} valores digitados é {soma}')
