quantidade_numeros = int(input('Quantos números você deseja inserir? '))

numeros = []

for i in range(quantidade_numeros):
    numero = float(input(f'Digite o {i+1}° número: '))
    numeros.append(numero)

soma = sum(numeros)
media = soma / quantidade_numeros

print(f'A média aritmetica dos números é: {media}')