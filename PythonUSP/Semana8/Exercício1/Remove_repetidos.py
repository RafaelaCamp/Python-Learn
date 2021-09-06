# Exercício 1 - Removendo elementos repetidos

# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

# Exemplo:
# 1 >>>lista = [2, 4, 2, 2, 3, 3, 1]
# 2 >>>remove_repetidos(lista)
# 3 [1, 2, 3, 4]
# 4 >>>remove_repetidos([1, 2, 3, 3, 3, 4])
# 5 [1, 2, 3, 4]

def remove_repetidos(lista): #def lista antes e colocar sort() apenas vai deixar a lista original ordenada, não a cópia.
    norepeat = []
    for i in lista:
        if i not in norepeat:
            norepeat.append(i)
    norepeat.sort()
    return norepeat

remove_repetidos([2, 2 , 1, 3])