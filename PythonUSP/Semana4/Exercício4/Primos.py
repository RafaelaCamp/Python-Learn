# Exercício 4 - Primos

# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

# Exemplos:
# 1 Digite um número inteiro: 13
# 2 primo

# 1 Digite um número inteiro: 12
# 2 não primo

n = int(input("Digite um número inteiro: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("não primo")