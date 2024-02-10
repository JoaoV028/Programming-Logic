v = [0] * 10

for c in range (1,11):
    print (f'Digite o {c}° valor: ',end='')
    v[c-1] = int(input())

for c in range(1,11):
    print (f'({c}, {v[c-1]})' , end='') 