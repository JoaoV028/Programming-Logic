while True:
    print (' ')
    print ('=' * 18)
    print ('|     M E N U    |')
    print ('=' * 18)
    r = int(input ('| [1] De 1 a 10  |\n| [2] De 10 a 1  |\n| [3] Sair       |\n'))
    if r == 1:
        c = 1
        while c <= 10:
            print (f'{c}..', end=(' '))
            c += 1
    if r == 2:
        c = 10
        while 1 <= c:
            print (f'{c}..',end=(' '))
            c -= 1
    if r == 3:
        print ('Obrigado por usar o programa!\nFIM!')
        break