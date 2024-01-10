print ('-' * 20)
print ('ESCOLA JAVALI CANSADO')
print ('-' * 20)
nt1 = float(input('Primeira Nota: '))
nt2 = float(input('Segunda Nota: '))
print('-' * 20)
med = (nt1 + nt2) / 2
print (f'MEDIA: {med:.2f}')
if med >= 7:
    print ('ALUNO APROVADO')
else: 
    print ('ALUNO REPROVADO')
print ('-' * 20)