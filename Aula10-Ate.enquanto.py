soma = 0
while True:
    numero = int(input('Digite o valor ==> '))
    soma += numero
    resposta = input('Você quer continuar? (S/N) ').upper()
    if resposta == 'N':
        break
print(f'A soma de todos os valores digitados é {soma}!')