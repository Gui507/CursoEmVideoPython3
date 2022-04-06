def sorteia(q, list):
    from random import randint
    c = 0
    while c < q:
        n = randint(0, 10)
        list.append(n)
        c +=1


def somapar(list):
    s = 0
    for n in list:
        if n % 2 == 0:
            s += n
    print(s)


from time import sleep
nums = []
sorteia(5, nums)
print('Soreteando 5 valores: ', end='')
for n in nums:
    print(f'{n} ', end='')
    sleep(0.25)
print()
print(f'somando os valores pares de {nums}, temos ',end='')
somapar(nums)