from time import sleep
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('Escolha oque voce deseja fazer:\n'
          '[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do programa ')
    opcao = int(input('Digite sua escolha: '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}')
    elif opcao == 2:
        produto = num1 * num2
        print(f'O produto entre {num1} e {num2} é {produto}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
            print(f'O maior número digitado foi {maior}')
        elif num1 == num2:
            print('Os dois valores são iguais')
    elif opcao == 4:
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite mais um: '))
    elif opcao > 5 or opcao == 0:
        print('Opção invalida, tente novamente')
    sleep(2)
print('Obrigado por me usar, tenha um bom dia')