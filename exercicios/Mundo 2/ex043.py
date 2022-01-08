p = float(input('Qual é o seu peso? '))
a = float(input('Qual é a sua altura? '))
imc = p / (a ** 2)
print('Seu imc é {:.1f} kg/m², estado:'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade modbida')
m = 18.5 * a ** 2
M = 25 * a ** 2
if 18.5 < imc < 25:
    print('Podendo variar entre {:.1f} e {:.1f} kg.'.format(m, M))
else:
    print('Seu peso ideal está entre {:.1f} e {:.1f} kg.'.format(m, M))
