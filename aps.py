import csv
from funcoes import *

longitudes = []
latitudes = []
distancias = []

with open('C:\\Users\\joaov\\OneDrive\\Documentos\\trabalho aps ordenação\\APS-ordena-o-4-semestre\\fotos.csv', 'r', newline='') as csvfile:
    arquivo = csv.DictReader(csvfile)
    for item in arquivo:
        longitude = float(item['longitude'])
        latitude = float(item['latitude'])

        longitudes.append(longitude)
        latitudes.append(latitude)

        distancia = calcular_distancia(latitude, longitude)
        distancias.append(distancia)

#arquivo_distancia(longitudes, latitudes, distancias)

menu()

while True:
    try:
        opcao = int(input("Digite o número da opção desejada (1 a 4): "))
        if opcao < 1 or opcao > 4:
            print("Por favor, escolha um número entre 1 e 4.")
        else:
            break
    except ValueError:
        print("Digite um número válido!")

if opcao == 2:
    bubble = bubble_sort(distancias)
    insertion_sort(distancias)
    selection_sort(distancias)
    merge_sort(distancias)
    quick_sort(distancias)
    shell_sort(distancias)