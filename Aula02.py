
'''
N1 = int(input('Digite um numero:'))
N2 = int(input('Digite outro numero:'))
R = N1 + N2
print (f'A soma de {N1} mais {N2} é igual a {R}')
'''
# Usando a ordem de precedencia dos operadores aritimetricos para descobrir a media:

def media (a, b):
    """Calcula a média de dois números"""
    m = (a + b) / 2
    return m #Retorna a média calculada

# Solicita ao usuário que digite dois números
n1 = int(input ('Digite um número: '))
n2 = int(input ('Digite outro número: '))

# Calcula a média usando a função definida anteriormente
resultado_media = media (n1, n2)

# iMprime o resultado
print (f'A média de {n1} e {n2} é {resultado_media}!')