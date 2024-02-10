def fatorial(n):
    r = 1
    for c in range (1, n + 1):
        r = r * c
    return r

n = int(input('Digite um número: '))
f = fatorial(n)

print(f'O fatorial de {n}! é igual a {f}!')
