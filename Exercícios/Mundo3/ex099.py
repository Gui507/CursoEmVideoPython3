from time import sleep
def maior(* num):
    print('-'*40)
    print(f'Analisando os valores passados.....')
    for n in num:
        print(f'{n} ',end='')
        sleep(0.25)
    print(f'foram informado {len(num)} valores ao todo.')
    ordem = sorted(num, reverse=True)
    print(f'O maior valor informado foi {ordem[0]}')
    print('-'*40)
    sleep(0.5)

maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)