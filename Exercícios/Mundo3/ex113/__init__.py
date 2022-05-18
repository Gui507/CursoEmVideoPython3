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


def leiafloat(msg):
   while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except ValueError or TypeError:
            print('\033[31mO valor informado é invalído, tente novamente\033[m')
        except KeyboardInterrupt:
            print('\nO usúario preferiu não digitar o valor')
            return 0
        else:
            return float(n)