# Exercício 1 - Fatorial

# Escreva um programa que receba um número natural n n n na entrada e imprima n! n! n! (fatorial) na saída.

# Exemplo:

# 1 Digite o valor de n: 5
# 2 120

# Dica: lembre-se que o fatorial de 0 vale 1!

n = int(input("Digite um número inteiro:"))
resultado = 1

for i in range (1, n +1):
  resultado *= i

print(resultado)
