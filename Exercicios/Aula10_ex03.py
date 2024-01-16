while True:
    n = int(input('Digite um numero: '))
    c = n
    f = 1
    while c >= 1:
        print (f'{c}x ', end='')
        f = f * c
        c -= 1
    print (f'\nO valor do fatorial de {n} é igual a {f}.')
    R = str(input('Quer continuar? (S/N)').upper())
    if R == 'N':
        break
