pes = float(input('Digite seu peso (Kg): '))
alt = float(input('Digite sua altura (M): '))
imc = pes / (alt ** 2)
print (f'Seu IMC é {imc:.2f}!')
if imc >= 18.5 and imc < 25:
    print('você está no peso ideal!')
if imc <= 18.5:
    print ('Você não esta na faixA de peso ideal!')
if imc > 25:
    print ('Você não esta na faixa de peso ideal!')