import csv
from funcoes import *
import time

algoritmo = []
inicio = []
fim = []
total = []
longitudes = []
latitudes = []
distancias = []
funcoes_ordenacao = [bubble_sort, insertion_sort,selection_sort, merge_sort, quick_sort, shell_sort, binary_insertion_sort,heap_sort,bucket_sort]

with open('fotos.csv', 'r', newline='') as csvfile:
    arquivo = csv.DictReader(csvfile)
    for item in arquivo:
        longitude = float(item['longitude'])
        latitude = float(item['latitude'])

        longitudes.append(longitude)
        latitudes.append(latitude)

        distancia = calcular_distancia(latitude, longitude)
        distancias.append(distancia)

# arquivo_distancia(longitudes, latitudes, distancias)

while True:
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

    if opcao == 1:
        comparar_dois(distancias)

        print("")
        opcao = input("Deseja continuar no programa?(S/N) ")
        if opcao == "N":
            break
        else:
            print("Voltando para a tela inicial...")
        limpartela()

    if opcao == 2:
        while funcoes_ordenacao:
            aleatoria = random.choice(funcoes_ordenacao)
            lista_ordenada, tempo_inicio, tempo_fim, tempo_total, nome_algoritmo = aleatoria(
                distancias.copy())

            algoritmo.append(nome_algoritmo)
            inicio.append(tempo_inicio)
            fim.append(tempo_fim)
            total.append(tempo_total)

            funcoes_ordenacao.remove(aleatoria)

            time.sleep(2)

        resultado(algoritmo, inicio, fim, total)
        for nome, tempo in zip(algoritmo, total):
            print("Nome do algoritmo:", nome)
            print("Tempo total:", tempo)
        conexao()

        print("")
        opcao = input("Deseja continuar no programa?(S/N) ")
        if opcao == "N":
            break
        else:
            print("Voltando para a tela inicial...")
        limpartela()

    elif opcao == 3:
        menor_distancia(distancias)

        print("")
        opcao = input("Deseja continuar no programa?(S/N) ")
        if opcao == "N":
            break
        else:
            print("Voltando para a tela inicial...")
        limpartela()

    elif opcao == 4:
        print("Saindo...")
        break
