##Coleta
n = int(input('Digite um número '))
print('Escolha a base de conversão')
print('[1] Binário\n[2] Octal\n[3] Hexadecimal')
b = int(input())
##Analise e Conversão
if b == 1:
    print(bin(n)[2:])
elif b == 2:
    print(oct(n)[2:])
elif b == 3:
    print(hex(n)[2:])
else:
    print('Opção Inválida')