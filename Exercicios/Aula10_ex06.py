homens_castanhos = 0
mulheres_loiras = 0
while True:
    print ('=' * 24)
    print ('   SELETOR DE PESSOAS   ')
    print ('=' * 24)

    while True:
        s = str(input('Qaul o sexo? [M/F] ')).upper()
        if s in ['M', 'F']:
            break
        print ('Entrada inválida. Por favor , insara M ou F.')

    while True:
        try:
            idade = int(input('Qual a idade? '))
            break
        except ValueError:
            print ('Entrada inválida. Por favir, insira um número.')

    while True:
        print ('[1] Preto\n[2] Castanho\n[3] Loiro\n[4] Ruivo')
        cor_do_cabelo = input('Qual a cor do cabelo? ')
        if cor_do_cabelo in ['1', '2', '3', '4']:
            break        
        print ('Entrada inválida. Por favor, insira um número de 1 a 4.')

    if s == 'M' and idade > 18 and cor_do_cabelo == '2':
        homens_castanhos += 1

    elif s == 'F' and 25 <= idade <= 30 and cor_do_cabelo == '3':
        mulheres_loiras += 1

    while True:
        r = str(input('Quer continuar? [S/N]\n' )).upper()
        if r in ['S', 'N']:
            break
        print ('Entrada inválida. Por favor, insira S ou N. ')
    if r == 'N':
        break
    
    print ('=' * 24)
    print ('RESULTADO FINAL')
    print ('=' * 24)
    print (f'Total de homens com mais de 18 e cabelos castanhos: {homens_castanhos}')
    print (f'Total de mulheres entre 25 e 30 ee cabelos loiros: {mulheres_loiras}')