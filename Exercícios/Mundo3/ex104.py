def leiaint(n):
    while n.isnumeric() == False:
        n = input('\033[31mERRO! Digite um número inteiro válido: \033[m')
    return n


n = leiaint(input('Digite um número: '))
print(f'Você digitou o número {n}')