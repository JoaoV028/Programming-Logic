c = 1
totn = 0
while c <= 5:
    n = int(input('Digite um número: '))
    if n < 0:
        totn = totn + 1
    c += 1
print (f'Foram digitados {totn} valores negativos!')