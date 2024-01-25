import math
def radiano (angulo_graus):
    """Converte um ângulo de graus para radianos."""

    return angulo_graus * math.pi / 180
# Solicita ao usuário que digite o ângulo em graus

angulo_graus = float(input('Digite o ângulo em graus: '))
# calcula o angulo em radianos usando a funçâo definida anteriormente

angulo_radianos = radiano (angulo_graus)

# Imprime o resultado 
print(f'O ângulo de {angulo_graus} graus é apriximadamente  {angulo_radianos:.2f} em radianos!')