import time

cont = 0
val = int(input('Quer contar até quanto? '))
salt = int(input('Qual sera o valor do salto? '))
while cont <= val:
    cont += salt
    print(cont - salt)
    time.sleep(0.8)
print ('Tá aí chefe!')