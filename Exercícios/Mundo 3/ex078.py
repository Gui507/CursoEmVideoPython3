n = [int(input('Digite um valor ')),int(input('Digite outro valor ')),
     int(input('Digite mais um valor ')), int(input('Digite mais um valor ')),
     int(input('Digite um último valor '))]
print(f'Você digitou os números\n{n}')
print(f'o maior valor foi {max(n)}, na posição {n.index(max(n)) + 1}')
print(f'o maior valor foi {min(n)}, na posição {n.index(min(n)) + 1}')
