# Exercício 6 - Distância entre dois pontos

# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

# longe

# na saída. Caso o contrário, quando a distância for menor que 10, imprima

# perto

# Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte:

# √ d(x,y)=(x1−x2)2+(y1−y2)2 d(x, y)'
​
import math

def Entrada(PC, coordenada):
    return float(input("Forneça a coordenada {} para o Plano Cartesiano {}: ".format(coordenada, PC))) # PC = PLANO CARTESIANO

PCA = Entrada("A", "X"), Entrada("A", "Y")
PCB = Entrada("B", "X"), Entrada("B", "Y")

Calculo = (PCA[0]-PCB[0])**2 + (PCA[1]-PCB[1])**2
distancia = math.sqrt(Calculo)

print("longe" if distancia >= 10 else "perto")