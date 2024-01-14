

print ('-' * 23)
print ('Escola Santa Paciencia')
print ('-' * 23)
q = int(input('Quantos alunos tem? '))
print ('-' * 20)
c = 1
notas = {}
mel_alu = ''
mel_not = 0
while c <= q:
    alu = str(input('Nome do aluno: '))
    nt = int( input (f'Nota de {alu}: '))
    print ('-' * 15)
    notas[alu] = nt
    if nt > mel_not:
        mel_not = nt
        mel_alu = alu
    c = c + 1

print (notas)
print(f'O melhor aproveitamento foi de {mel_alu} com {mel_not}!')