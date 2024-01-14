# TEM QUE TER INICIO (numero)
# TEM Q TER UM FIM (numero)
# PRECISA CONTAR DE CMÇ AO FIM
# MOSTRAR QUE ESTA CONTANDO EM LINHA RETA
# SE CMÇ + = SUBTRAIR
# SE CMÇ - = SOMAR
import time

print('CONTAGEM INTELIGENTE')
print('-' * 22)
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
time.sleep(0.8)
print('-' * 18)
print('C O N T A N D O')
print('-' * 18)

if inicio > fim:
    c = inicio
    while c >= fim:
        print(c)
        c -= 1
        time.sleep(0.8)
else:
    c = inicio
    while c <= fim:
        print(c)
        c += 1
        time.sleep(0.8)