# Exercício 4 - (Difícil) Soma das hipotenusas

# Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras, nnn é uma hipotenusa se existem números inteiros iii e jjj tais que:

# n2=i2+j2 n^2 = i^2 + j^2 n2=i2+j2

# Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n n n e devolva a soma de todos os inteiros entre 1 e n n n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

# Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até n n n testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

# Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

# Exemplo: 

# 1 Para n = 25, as hipotenusas são:
# 2 5, 10, 13, 15, 17, 20, 25
# 3 note que cada número deve ser somado apenas uma vez. Assim:
# 4 soma_hipotenusas(25)
# 5 deve devolver 105


def e_hipotenusa(a, b):
    hipotenusa = ((a **2) + (b **2))
    return hipotenusa


def soma_hipotenusas(n):
    c = 1
    soma = 0
    for c in range(n+1):
        c2 = c**2
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if c2 == e_hipotenusa(a, b):
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1
    return soma

# "nunca um código me fez sentir tão BURRO"