# Exercício 2 - Primos

# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

# Exemplos de execução no shell do Python:

# 1 >>> maior_primo(100)
# 2 97
# 3 >>> maior_primo(7)
# 4 7
def maior_primo(n):

    primos = []
    for i in range(n+1): # +1 depois de n pois se não a variável i vai de 0 até n-1 (ou seja, o n não é incluído). Por isso, seu programa acaba não incluindo o número do parâmetro em si
        c = 0
        for j in range(n):
            if i%(j+1) == 0:
                c += 1
        if c == 2:
            primos.append(i)

    print(max(primos))

