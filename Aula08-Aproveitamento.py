# A = 10 - 9, B = 9 - 8, C = 8 - 7, D = 7 - 6, E = 6 - 5, F 5 >
A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
print('-' * 20)
print('   JAVALI CANSADO   ')
print ('-' * 20)
n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
print ('-' * 20)
med = (n1 + n2) / 2

if med >= 9:
    aprov = A
elif med >= 8:
    aprov = B
elif med >= 7:
    aprov = C
elif med >= 6:
    aprov = D
elif med >= 5:
    aprov = E
else:
    aprov = F

print (f'MEDIA: {med:.2f}')
print (f'APROVEITAMENTO: {aprov}')
print ('-' * 20)