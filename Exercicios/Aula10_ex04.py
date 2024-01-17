c = 1
n = int(input('Digite um numero: '))
contv = 0
while c <= n:
    if n % c == 0:
        contv = contv + 1
    print (c, end=(' '))
    c += 1
if contv > 2:
     print (f'\nO valor de {n} não é primo!')
else:
      print(f'\nO valor de {n} é primo!')