# Inicializando a lista e as variáveis
soc = [''] * 10
tot = 0

# Loop de 0 a 9 (equivalente a 1 a 10 no seu código original)
for c in range (10):
    nome = input('Digite seu nome: ')

# Verifica se a primeira letra do nome é 'C'
    if nome[0].upper() == 'C':
        soc[tot] = nome
        tot += 1

# Limpa a tela (no terminal)
print ('\033c', end= '')

print ('LISTAGEM FINAL')
for c in range (tot):
    print (soc[c])