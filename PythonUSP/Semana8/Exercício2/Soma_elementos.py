# Exercício 2 - Soma dos elementos de uma lista

# Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

def soma_elementos(lista):
    soma = sum([])
    for i in lista:
        soma += i
    print(soma)

soma_elementos ([1, 2, 3, 6])