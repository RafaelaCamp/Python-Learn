# Exercício 3 - Vogais

# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

# Exemplos de execução no shell de Python

# 1 >>> vogal("a")
# 2 True
# 3 >>> vogal("b")
# 4 False
# 5 >>> vogal("E")
# 6 True

# Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

# Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

def vogal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x== "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return(True)
    else:
        return(False)
