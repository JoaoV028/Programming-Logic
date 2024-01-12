pes = float(input('Digite seu peso (Kg): '))
alt = float( input('Digite sua altura (M): '))
imc = pes / (alt ** 2)
print (f'Seu IMC é de {imc:.2f}.')
if imc < 17:
    print ('Muito abaixo do peso.')
else:
    if imc >= 17 and imc <= 18.5:
        print ('Abaixo do peso.')
    else:
        if imc >= 18.5 and imc <= 25:
            print ('Peso ideal.')
        else:
            if imc >= 25 and imc <= 30:
                print ('Sobrepeso')
            else:
                if imc >= 30 and imc <= 35:
                    print ('Obesidade')
                else:
                    if imc >= 35 and imc <= 40:
                        print ('Obesidade severa')
                    else: 
                        if imc >= 40:
                            print ('Obsidade mórmida')