n = int(input('escreva um número'))
print('Selecione a base de conversão')
print('[1] Binário\n'
      '[2] Octal\n'
      '[3] Hexadecimal')
c = int(input())
if c == 1:
      print('{} em binário é {}'.format(n, bin(n)[2:]))
elif c == 2:
      print('{} em octal é {}'.format(n, oct(n)[2:]))
elif c == 3:
      print('{} em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
      print('opcão inválida')