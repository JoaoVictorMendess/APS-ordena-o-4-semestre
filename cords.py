import math


def haversine(coord1, coord2):
    # Raio da Terra em quilômetros
    R = 6371.0

    # Coordenadas em radianos
    lat1 = math.radians(coord1[0])
    lon1 = math.radians(coord1[1])
    lat2 = math.radians(coord2[0])
    lon2 = math.radians(coord2[1])

    # Diferenças das coordenadas
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula do Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Distância em quilômetros
    distance = R * c
    return distance


# Exemplo de uso
coordenada1 = (40.7128, -74.0060)  # Nova York
coordenada2 = (34.0522, -118.2437)  # Los Angeles

distancia = haversine(coordenada1, coordenada2)
print(f"A distância entre as duas coordenadas é: {distancia:.2f} km")
