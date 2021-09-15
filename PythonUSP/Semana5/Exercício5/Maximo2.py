# Exercício 5 - Máximo com 3 parâmetros

# Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

# Exemplos de execução no Python Shell
# 1 >>>maximo(30, 14, 10)
# 2 30
# 3 >>>maximo(0, -1, 1)
# 4 1

def maximo(x, y, z):

    lista = sorted([x, y, z]) # sorted() vai ordenar as informações da lista
    maior = lista[-1] # ultima posição
    return(maior)