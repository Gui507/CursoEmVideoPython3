from Exercícios.Mundo3.ex108 import moeda
p = float(input('Digite o preço R$'))
print(f'A metade de R${p:.2f} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${p:.2f} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% fica {moeda.moeda(moeda.aumentar(p, 10))} ')
print(f'Dimnuindo 10% fica {moeda.moeda(moeda.diminuir(p, 10))}')
