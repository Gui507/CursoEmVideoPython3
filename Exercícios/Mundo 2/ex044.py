p = float(input('Qual é o valor do produto? R$ '))
f = int(input('Selecione a forma de pagamento:\n[1] À vista\n[2] Cartão\n'))
if f == 1:
    print('O valor a ser pago será R${:.2f}'.format(p-(p*0.10)))
elif f == 2:
    c = int(input('[1] À vista\n[2] Parcelado\n'))
    if c == 1:
        print('o valor a ser pago será R${:.2f}'.format(p-(p*0.05)))
    elif c == 2:
        d = int(input('Digite o numéro de parcelas '))
        if d <= 2:
            print('o valor a ser pago será R${:.2f} com parcelas de R${:.2f}'.format(p, p/d))
        else:
            print('O valor a ser pago será R${:.2f} com parcelas de R${:.2f}'.format(p+(p*0.20), p/d))