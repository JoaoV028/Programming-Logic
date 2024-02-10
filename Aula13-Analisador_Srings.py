import string

n = input('Digite seu nome: ')
print ('Total de letras do seu nome: ', len(n))
print ('Seu nome em maiúsculas é ',n.upper())
print ('Seu nome em minúsculas é ',n.lower())
print ('A primeira letra do seu nome é', n[0])
print ('A última lettra do seu nome é ', n[-1].upper())
if 'A' in n.upper():
    print ('Seu nome tem a letra A na posição ', n.upper().index('A') + 1)
else:
    print ('A letra A nã ofoi encontrada no seu nome')

print ('O código da letra A é ', ord('A'))

print ('A  legtra de código 65 é ', chr(65))


for c in range(len(n) -1,-1,-1):
    print (n[c].upper())