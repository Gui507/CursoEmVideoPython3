extenso =('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
          'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número de 0 a 20 '))
while n not in range(0,21):
    n = int(input('Opção inválida. Digite um número de 0 a 20 '))
print(f'Você digitou o número {extenso[n]}')
