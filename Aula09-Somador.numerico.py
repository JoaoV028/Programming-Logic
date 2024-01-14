import time

maior = 0
cont = 1
s = 0
menor = 0
while cont < 6:
    N = int (input (f'Digite o {cont}° valor: '))
    if N >= maior :
        maior = N
    if cont == 1 or N < menor:
        menor = N
    cont += 1
    s = s + N
    time.sleep(0.5)
print (f'A soma dos valores foi de {s}!')
print (f'O maior número foi {maior}!')
print (f'O menor número foi {menor}!')