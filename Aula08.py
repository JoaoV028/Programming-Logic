n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota do aluno:'))
m = (n1 + n2) / 2
print (f"Sua média é {m:.2f}!")
if m >= 7:
    print ('Parabéns! Você passou!')
else:
    if m >= 5 and m <= 7:
     print ('Você está de recuperação!')
    else:
       print ('Você está de recuperação!')