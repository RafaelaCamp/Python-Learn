# Exercício 4 - Invertendo sequência

# Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

# Exemplo:

# 1 Digite um número: 1
# 2 Digite um número: 7
# 3 Digite um número: 4
# 4 Digite um número: 0
# 5
# 6 4
# 7 7
# 8 1

seq = [] # defina a sequencia em lista
while True:
    n = (int(input("Digite um número:")))
    if (n != 0):
        seq.append(n)
    else:
        break
for i in seq [:: -1]:
    print(i)