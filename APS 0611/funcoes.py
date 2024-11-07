import math
import random
import csv
import time
from datetime import datetime

# Função Bubble Sort
def bubble_sort(a):
    algoritmo = 'BubbleSort'
    inicio = time.time()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    fim = time.time()
    total = fim - inicio

    #Formatando hora
    inicio_formatado = datetime.fromtimestamp(inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return a, inicio_formatado, fim_formatado, total, algoritmo


# Função Insertion Sort
def insertion_sort(a):
    algoritmo = 'InsertionSort'
    inicio = time.time()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    fim = time.time()
    total = fim - inicio

    #Formatando hora
    inicio_formatado = datetime.fromtimestamp(inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return a, inicio_formatado, fim_formatado, total, algoritmo


# Função Selection Sort
def selection_sort(a):
    algoritmo = 'SelectionSort'
    inicio = time.time()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    fim = time.time()
    total = fim - inicio

    #Formatando hora
    inicio_formatado = datetime.fromtimestamp(inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return a, inicio_formatado, fim_formatado, total, algoritmo


# Função Merge Sort
def merge_sort(a):
    algoritmo = 'Merge Sort'
    inicio = time.time()
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
    fim = time.time()
    total = fim - inicio
    
    #Formatando hora
    inicio_formatado = datetime.fromtimestamp(inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return a, inicio_formatado, fim_formatado, total, algoritmo


# Função Quick Sort
def quick_sort(lista):
    # Marcar o tempo de início
    inicio = time.time()

    if len(lista) <= 1:
        return lista, inicio, time.time(), 0, 'QuickSort' 
    pivo = lista[len(lista) // 2]
    esq = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]

    lista_ordenada = quick_sort(esq)[0] + meio + quick_sort(direita)[0]
    
    fim = time.time()
    total = fim - inicio
    algoritmo = 'QuickSort'
    
    #Formatando hora
    inicio_formatado = datetime.fromtimestamp(inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return lista_ordenada, inicio_formatado, fim_formatado, total, algoritmo


# Função Shell Sort
def shell_sort(a):
    algoritmo = 'ShellSort'
    inicio = time.time()
    n = len(a)
    diff = n // 2
    while diff > 0:
        for i in range(diff, n):
            temp = a[i]
            j = i
            while j >= diff and a[j - diff] > temp:
                a[j] = a[j - diff]
                j -= diff
            a[j] = temp
        diff //= 2
    fim = time.time()
    total = fim - inicio

    #Formatando hora
    inicio_formatado = datetime.fromtimestamp(inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return a, inicio_formatado, fim_formatado, total, algoritmo


def calcular_distancia(x, y):
    distancia = math.sqrt(x ** 2 + y ** 2)
    return distancia


def calcular_raio(distancia):
    raio = distancia / 2
    return raio


def arquivo_distancia(latitudes, longitudes, distancias):
    with open('fotos_dist.csv', 'w', newline='') as csvfile:
        colunas = ['latitude', 'longitude', 'distancia']
        escrever = csv.DictWriter(csvfile, fieldnames=colunas)
        
        escrever.writeheader()
        
        for lat, lon, dist in zip(latitudes, longitudes, distancias):
            escrever.writerow({'latitude': lat, 'longitude': lon, 'distancia': dist})

    print("Distâncias calculadas e salvas em fotos_com_distancia.csv")
    
def calc_tempo(alg, lista):
    inicio = time.time()
    alg(lista)
    fim = time.time()
    return fim - inicio

    
def comparar_dois(lista):
    metodos = [bubble_sort, insertion_sort, selection_sort, quick_sort, merge_sort]

    met1, met2 = random.sample(metodos, 2)

    tempo1 = calc_tempo(met1, lista)
    time.sleep(2)
    tempo2 = calc_tempo(met2, lista)
    
    print(f"Método 1: {met1.__name__}")
    print(f"Método 2: {met2.__name__}")
    
    print(f"Tempo de execução do método {met1.__name__}: {tempo1:.19f} segundos")
    print(f"Tempo de execução do método {met2.__name__}: {tempo2:.19f} segundos")

    if tempo1 < tempo2:
        print(f"O método {met1.__name__} foi mais rápido!")
    elif tempo1 > tempo2:
        print(f"O método {met2.__name__} foi mais rápido!")
    else:
        print("Ambos os algoritmos tiveram o mesmo tempo de execução!")

    print("Distâncias calculadas e salvas em fotos_com_distancia.csv")


def resultado(algoritmo, inicio, fim, total):
    with open('arquivo_final.csv', 'w', newline='') as arquivo:
        colunas = ['Algoritmo','Ínicio', 'Fim', 'Tempo Total']
        escrever = csv.DictWriter(arquivo, fieldnames=colunas)

        escrever.writeheader()

        for algoritmo, inicio, fim, total in zip(algoritmo, inicio, fim, total):
            escrever.writerow({'Algoritmo':algoritmo, 'Ínicio':inicio, 'Fim':fim, 'Tempo Total':total})

def menor_distancia(lista):
    menor_distancia = lista[0]

    for distancia in lista[1:]:
        if distancia < menor_distancia:
            menor_distancia = distancia

    print("Menor distância:", menor_distancia)

def menu():
    print("1 - Comparar Dois")
    print("2 - Executar Todos")
    print("3 - Buscar Menor Distância")
    print("4 - Sair")
