# Solicita ao usuário o valor principal e a taxa de juros
ve = float(input('Digite o valor que deseja pegar: '))
ju = float(input('Digite o valor do juros:'))

# Calcula o valor total com juros
nve = ((ve * ju) / 100) + ve
print (f'O valor total vai ser R${nve:.2f}!')

# Solicita ao usuário o número de parcelas
parc = int(input('Digite o número de parcelas:'))

# Se o número de parcelas for maior que 12, solicita ao usuário um novo número
while parc > 12:
    print('Desculpe, o número máximo de parcelas é 12.')
    parc = int(input('Digite o número de parcelas')) 

# Calcula o valor de cada parcela
valor_parc = nve / parc

# Exibe o valor de cada parcela
print (f'O valor de cada parcela será de R${valor_parc:.2f} se você optar por parcelar em {parc}x')
