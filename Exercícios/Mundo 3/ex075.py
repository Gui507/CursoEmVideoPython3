valores = (int(input('Digite um valor: ')), int(input('Outro valor: ')), int(input('Outro valor: ')), int(input('Outro valor: ')))
print(f'Os valores digitados foram {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
print(f'o primeiro número 3 aparece na posição {valores.index(3)+1}' if 3 in valores else 'O número 3 não apareceu')
print('Os números pares foram: ', end='')
for c in valores:
    if c %2 == 0:
        print(f'{c}  ', end='')
