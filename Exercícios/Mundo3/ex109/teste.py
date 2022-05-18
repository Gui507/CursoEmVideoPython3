from Exercícios.Mundo3.ex109 import moeda

p = float(input('Digite o preço R$'))
print(f'A metade de R${moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% fica {moeda.aumentar(p, 10, True)} ')
print(f'Dimnuindo 10% fica {moeda.diminuir(p, 10, True)}')
