print('Analisador de triângulos')
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Esses segmentos formam um triângulo equilátero')
    elif r1 != r2 != r3 != r1 :
        print('Esses segmentos formam um triâmgulo escaleno')
    else:
        print('Esses segmentos formam um triângulo isósceles')
else:
    print('Esses segmentos, não formam um triângulo.')
    