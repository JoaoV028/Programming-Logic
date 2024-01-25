def detector_pesado():
    maior_peso = 0
    nome_pesado = ''

    for i in range (5):
        nome = str(input('Digite o nome: '))

        while True:
            try:            
                peso = float(input(f'Digite o peso de {nome} Kg: '))
                break
            except ValueError:
                print("Por favor, insira um número válido para o peso.")

            if peso > maior_peso:
                maior_peso = peso
                nome_pesado = nome

    print (f'DETECTOR DE PESADO')
    print (f'Maior Peso até agora: {maior_peso} Kg')
    print (f'Pessoa mais pesada : {nome_pesado}')

detector_pesado()
