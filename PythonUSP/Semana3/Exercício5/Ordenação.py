# Exercício 5 - Verificando ordenação

# Receba 3 números inteiros na entrada e imprima

# crescente

# se eles forem dados em ordem crescente. Caso contrário, imprima 

# não está em ordem crescente

n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))

if (n3 > n2 > n1):
  print("crescente")
else:
  print("não está em ordem crescente")