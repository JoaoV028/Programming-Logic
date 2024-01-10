ano = int(input('Em que ano estamos? '))
nasc = int(input('Em que ano você nasceu? '))
idade = ano - nasc
print (f'No ano {ano} você tera {idade} anos!')
if idade >= 20:
    print ('E você alcançou a maoir idade!')
else:
    print('E você não alcançou a maior idade!')