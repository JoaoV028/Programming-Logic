print ('=' * 26)
print ('DEPARTAMENTO DE TRANSITO')
print ('=' * 26)
ano = int(input('\nAno atual (yyyy): '))
nasc = int(input('Ano de Nascimento (yyyy): '))
idade = ano - nasc
print ('\n======== STATUS ========') 
print (f'IDADE: {idade} ANOS')
if idade >= 18:
    print ('APTO A  TIRAR A CARTEIRA')
else:
    print('NÃO APTO A TIRAR A CARTEIRA')
print ('=' * 24)