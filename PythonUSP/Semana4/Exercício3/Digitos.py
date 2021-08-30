# Exercício 3 - Soma dos Dígitos
# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

# Exemplo:

# 1 Digite um número inteiro: 123
# 2 6

#Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.

x = int(input("Digite um número:"))
soma = 0

while (x != 0):
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto
print(soma)