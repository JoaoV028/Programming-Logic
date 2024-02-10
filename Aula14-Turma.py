# Inicializando as listas
nome = [''] * 4
n1 = [0.0] * 4
n2 = [0.0] * 4
m = [0.0] * 4
sm = 0
mt = 0
tot = 0

# Loop de 0 a 3 (equivalente a 1 a 4 no seu código original)
for i in range(4):
    print (f'Aluno {i+1}°')
    nome[i] = input ('Nome: ')
# Verificação de entrada para a primeira nota
    while True:
        try:
            n1[i] = float(input ('Primeira nota: '))
            if 0 <= n1[i] <= 10 :
                break
            else:
                print('Por favor, insira uma nota entre 0 e 10.')
        except ValueError:
            print ('Por favor, insira um número válido.')

# Verificação de entrada para a segunda nota
    while True:
        try:
            n2[i] = float(input ('Segunda nota: '))
            if 0 <= n2[i] <= 10 :
                break
            else:
                print('Por favor, insira uma nota entre 0 e 10.')
        except ValueError:
            print('Por Favvor, insira um número válido.')

# Calcula a média das notas 
    m[i] = (n1[i] + n2[i]) / 2

    sm = sm + m[i]

mt = sm / 4
# Limpa a tela (no terminal)
print('\033c', end='')

# Imprime a lista de alunos
print('LISTAGM DOS ALUNOS')
print('=' * 20)
for c in range (4):
    print(nome[c],m[c])
    if (m[c] >= mt):
        tot += 1
print (f'Ao todo temos {tot} alunos acima da média da turma que é´{mt:4.1f}')
