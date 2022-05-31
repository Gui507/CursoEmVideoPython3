def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError or TypeError:
            print('\033[31mO valor informado é invalído, tente novamente\033[m')
        except KeyboardInterrupt:
            print('\nO usúario preferiu não digitar o valor')
            return 0
        else:
            return int(n)


def linha(tam=40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(list):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in list:
        print(f'\033[1:33m{c} - \033[34m{i}\033[m ')
        c += 1
    print(linha())
    return leiaint('\033[1:32mSua opção: \033[m')