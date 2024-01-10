import math

angulo = float(input('Digite o angulo:'))
angulo.radianos = angulo * math.pi / 180
print (f'O angulo de {angulo} graus é aproximadamente {angulo.radianos:4} em radianos!')