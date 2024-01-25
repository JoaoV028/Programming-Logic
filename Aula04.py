def formar_triangulo (l1, l2, l3):
    """Verifica se é possivel formar um triângulo com os comprimentos dos lados dados."""
    return l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2
def tipo_triangulo (l1, l2 , l3):
    '''Determina o tipo de triângulo com base nos comprimentos dos lados dados.'''
    if l1 == l2 == l3:
        return 'equilátero'
    elif l1 != l2 != l3 != l1:
        return 'escaleno'
    else:
        return 'isósceles'

# Solicita ao usuário que digite os  comprimentos dos lados do triângulo
l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))

# Verifica se é possìvel formar um triângulo e determina o tipo
if formar_triangulo (l1, l2, l3):
    print('É possível formar um triângulo!')
    print (f'O triângulo é {tipo_triangulo(l1, l2, l3)}.')
else: print('Não é possivel formar um triângulo!') 