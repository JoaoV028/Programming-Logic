import time

x = int( input ( 'Qauntas vezes você quer converter? ' ))
c  = 1
while c <= x:
    r = float (input ('Quanto você tem R$:  ') )
    dol = 2.22
    din = r / dol
    print (f'Você pode comprar US{din:.2f}!')
    c = c + 1
    time.sleep (0.8)