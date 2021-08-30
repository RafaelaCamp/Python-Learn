# Exercício 2 - ímpares

# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

# Exemplo:
# 1 Digite o valor de n: 5
# 2 1
# 3 3
# 4 5
# 5 7
# 6 9

n = int(input("Digite um número de sequência:"))
i = 0

while i < n:
    print(2*i+1)

    i = i + 1 