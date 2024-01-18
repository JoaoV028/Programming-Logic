Simp = 0
tot010 = 0
for c in range (1,7):
    v = int(input('Digite um valor: '))
    if v >= 0 and v <= 10 :
        tot010 = tot010 + 1
        if v % 2 == 1:
            Simp = Simp + v
print (f'Ao todo foram {tot010} valores entre 0 e 10!')
print (f'Ao total a soma de impares é  {Simp}!')