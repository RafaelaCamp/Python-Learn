# Exercício 5 - Desafio do vídeo "Repetição com while"

# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

# Exemplos:

# 1 Digite um número inteiro: 12345
# 2 não

# 1 Digite um número inteiro: 1011
# 2 sim

x = input('Insira um valor inteiro:')

tamanho = len(x)
verifica = False
i = 0

while i < tamanho - 1:
    if x[i] == x[i + 1]:
        verifica = True
    i += 1

if verifica:
    print("sim")
else:
    print("não")