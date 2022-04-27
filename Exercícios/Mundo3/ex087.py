matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = stcol = maiors = 0
# COLETA
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição[{l}, {c}]: '))
        #ANÁLISE
        if matriz[l][c] %2 == 0:
            spar += matriz[l][c]
        if matriz[l][2]:
            stcol += matriz[l][2]
        if matriz[1][c] > maiors:
            maiors = matriz[1][c]
# ESCREVER NA TELA
print('-'*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-'*40)
#RESULTADOS
print(f'A soma de todos os valores pares digitados é: {spar}')
print(f'A soma dos valores da terceira coluna é: {stcol}')
print(f'O maior valor da segunda linha é: {maiors}')
