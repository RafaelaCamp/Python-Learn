# Exercício 3 - Contagem de Primos

# Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

# Exemplo:
# 1   >>>n_primos(2)
# 2   1
# 3   >>>n_primos(4)
# 4   2
# 5   >>>n_primos(121)
# 6   30

def isPrime(n):
    # definir primeiro a função para encontrar os primos 
    # Corner case
    if n <= 1:
        return  False

    # check 2 ao n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Função para retornar primos
def n_primos(n):
    primo = []
    for i in range(2, n + 1):
        if isPrime(i):
            primo.append(i) #criar uma lista
    return (int(len(primo))) #retornar o total de números dentro da lista
                
#test
n_primos(6)