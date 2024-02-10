val = [0] * 7
totpar = 0
pp = []

for i in range (7):
    val[i] = int(input(f'Digite o {i + 1}° valor: '))
    if val[i] % 2 == 0 :
        totpar += 1
        pp.append(i+1)

print (f'O total de pares é {totpar}')
print (f'As posições dos valores parers são {pp}')