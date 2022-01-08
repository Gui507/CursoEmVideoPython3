n = int(input('Digite o primeiro termo da P.A '))
r = int(input('Digite a razão dessa P.A '))
c = 1
termo = n
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(termo, end=' → ')
        termo += r
        c += 1
    print('Pausa')
    mais = int(input('Deseja mais quantos termos? '))
print(f'Progressão finalizada com {total} termos')
print('Obrigado por me usar, tenha um bom dia')
