import math


def calcular_distancia(x1, y1, x2, y2): 
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia


def calcular_raio(distancia):
    raio = distancia / 2
    return raio


x1 = float(input("Digite o valor do X1:"))
y1 = float(input("Digite o valor do Y1:"))
x2 = float(input("Digite o valor do X2:"))
y2 = float(input("Digite o valor do Y2:"))

distancia = calcular_distancia(x1, y1, x2, y2)
raio = calcular_raio(distancia)

print("Distância", distancia)
print("Raio:", raio)
