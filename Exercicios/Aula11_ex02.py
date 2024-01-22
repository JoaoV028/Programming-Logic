c = 1
som = 0
med = 0
sdiv = 0
nulos = 0
spares = 0


for c in range (1,6):
    n = int(input(f'Digite o {c}°Numero: '))
    som = som + n
    if n % 5 == 0:
        sdiv += 1
    if n == 0:
        nulos += 1
    if n % 2 == 0:
        spares = spares + n
med = som / c
print (f'A soma dos valores é de {som}.\nA média dos valores é de {med}.\nOs números divisiveis por 5 são {sdiv}.\nO total de nulos é {nulos}.\nA soma dos pares é de {spares}.')