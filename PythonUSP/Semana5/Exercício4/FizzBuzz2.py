# Exercício 4 - FizzBuzz

# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

# 'Fizz' se o número for divisível por 3 e não for divisível por 5;

# 'Buzz' se o número for divisível por 5 e não for divisível por 3;

# 'FizzBuzz' se o número for divisível por 3 e por 5;

# Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

# Exemplos de execução no Python Shell
# 1 >>>fizzbuzz(3)
# 2 "Fizz"
# 3 >>>fizzbuzz(5)
# 4 "Buzz"
# 5 >>>fizzbuzz(15)
# 6 "FizzBuzz"
# 7 >>>fizzbuzz(4)
# 8 4

def fizzbuzz(x):
    if x%3 == 0 and x%5 == 0:
        return("FizzBuzz")
    elif (x%3) == 0:
        return("Fizz")
    elif (x%5) == 0:
        return("Buzz")
    else:
        return(x)