# Exercício 3 - Maior elemento de uma lista

# Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

def maior_elemento(lista):
    num = max(lista)
    return num

maior_elemento([1, 2, 3, 4, 5])