# Definindo a função 'par_ou_impar' que aceita um 
# número inteiro como argumento
def par_ou_impar (v):
    # Verificando se o número é par
    if v % 2 == 0 :
        return "Par"  # Se o número for par, a função retorna a string "PAR"
   
    else:
        return "Impar" # Se o número não for par (ou seja, é ímpar), a função retorna a string "IMPAR"
    
# Solicitando ao usuário para inserir um número
n = int(input('Digite um número: '))

# Chamando a função 'par_ou_impar' com 'n' como argumento e armazenando o resultado na variável 'r'
r = par_ou_impar (n)

# Imprimindo o resultado
print(f'O número é {r}.')