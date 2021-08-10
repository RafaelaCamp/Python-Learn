# Exercício 2 - Médias

# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

# Exemplo:

#    Entrada de Dados:

# Digite a primeira nota: 4

# Digite a segunda nota: 5

# Digite a terceira nota: 6

# Digite a quarta nota: 7

#    Saída de Dados:

# A média aritmética é 5.5

n1 = float(input("nota 1:"))
n2 = float(input("nota 2:"))
n3 = float(input("nota 3:"))
n4 = float(input("nota 4:"))

média = ((n1+n2+n3+n4)/4)
print("A Média Aritmética é:", média)