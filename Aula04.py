L1 = float(input('Digite o primeiro angulo: '))
L2 = float(input('Digite o segundo angulo: '))
L3 = float(input('Digite o terceiro angulo: '))

if L1 < (L2 + L3) and L2 < (L1 + L3) and L3 < (L2 + L1):
    print ('Pode formar um triangulo!')
    if L1 == L2 and L2 == L3:
        print('É um triangulo equilatero!')
    elif L1 != L2 and L2 != L3 and L1 != L3:
        print('É um triangulo escaleno!')
    else:
        print('É um triangulo isósceles!')
else:
    print ('Não pode formar um triangulo!')

if L1 == L2 and L2 == L3:
    print('Se formar um triangulo, será equilatero!')
else:
    print('Se formar um triangulo, não será equilatero!')

if L1 != L2 and L2 != L3 and L1 != L3:
    print('Se formar um triangulo, será escaleno!')
else:
    print('Se formar um triangulo, não será escaleno!')

if (L1 == L2 and L1 != L3) or (L1 == L3 and L1 != L2) or (L2 == L3 and L2 != L1):
    print('Se formar um triangulo, será isósceles!')
else:
    print('Se formar um triangulo, não será isósceles!')
