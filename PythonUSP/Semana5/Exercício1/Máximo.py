# Exercício 1 - Máximo

# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

# Exemplos de execução no shell do Python:
# 1 >>> maximo(3, 4)
# 2 4
# 3 >>> maximo(0, -1)
# 4 0


def maximo(x, y):

    if x > y:
        return(x)
    else:
        return(y)
