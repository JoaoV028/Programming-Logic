print ('=' * 25)
tm1 = str (input ('Nome do time 1:'))
tm2 = str (input ('Nome do time 2:'))
print('=' * 25)
print (f' Time {tm1} X Time {tm2}')
print ('=' * 25)
gl1 = int(input(f'Quantos gols do {tm1}?'))
gl2 = int(input(f'Quantos gols do {tm2}?'))
r = abs(gl1 - gl2)
if r == 0:
    print(f'A diferença foi de: {r}')
    print('STRATUS: EMPATE!')
elif r in [1,2,3]:
    print(f'A diferença foi de: {r}')
    print ('STATUS: Partida normal!')
else: print (f'A diferença foi de: {r}')
print ('STATUS: GOLEADA!')