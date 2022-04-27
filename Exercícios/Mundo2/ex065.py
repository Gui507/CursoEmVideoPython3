n = int(input('Digite um valor: '))
count = 0
o = str(input('Deseja continuar [S/N]? ')).strip()[0]
maior = menor = n
soma = n
while o not in 'Nn':
    n = int(input('Digite outro valor: '))
    o = str(input('Deseja continuar [S/N]? ')).strip()[0]
    count += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'A média entre os {count +1} numeros digitados foi {soma/(count+1)} onde, o maior valor é {maior} e o menor é {menor}')
