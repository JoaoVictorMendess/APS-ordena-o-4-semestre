import math
import random
import csv
import time
from datetime import datetime
import os
import platform
import psutil
import mysql.connector

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

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
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

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
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

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
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

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
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

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
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

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return a, inicio_formatado, fim_formatado, total, algoritmo


def binary_insertion_sort(arr):
    algoritmo = 'BinaryInsertionSort'
    inicio = time.time()
    """Ordena a lista 'arr' usando Binary Insertion Sort em uma única função."""
    for i in range(1, len(arr)):
        val = arr[i]
        # Busca binária para encontrar a posição correta
        start, end = 0, i
        while start < end:
            mid = (start + end) // 2
            if arr[mid] < val:
                start = mid + 1
            else:
                end = mid
        # Move os elementos e insere 'val' na posição encontrada
        arr[start+1:i+1] = arr[start:i]
        arr[start] = val
    fim = time.time()
    total = fim - inicio

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return arr, inicio_formatado, fim_formatado, total, algoritmo


def heap_sort(arr):
    algoritmo = 'HeapSort'
    inicio = time.time()
    """Ordena a lista 'arr' usando HeapSort."""
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Constrói o heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos do heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    fim = time.time()
    total = fim - inicio

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return arr, inicio_formatado, fim_formatado, total, algoritmo


def bucket_sort(arr):
    algoritmo = 'BucketSort'
    inicio = time.time()
    """Ordena a lista 'arr' usando Bucket Sort."""
    if len(arr) == 0:
        return arr

    # Passo 1: Encontrar o intervalo de valores
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / len(arr)  # Tamanho de cada bucket

    # Passo 2: Criar e distribuir os elementos nos buckets
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        index = int((num - min_val) // bucket_range)
        if index == len(arr):  # Garante que o último valor vá para o último bucket
            index -= 1
        buckets[index].append(num)

    # Passo 3: Ordenar cada bucket e concatenar os resultados
    sorted_arr = []
    for bucket in buckets:
        # Usando sorted() para ordenar cada bucket
        sorted_arr.extend(sorted(bucket))

    fim = time.time()
    total = fim - inicio

    # Formatando hora
    inicio_formatado = datetime.fromtimestamp(
        inicio).strftime('%Y-%m-%d %H:%M:%S')
    fim_formatado = datetime.fromtimestamp(fim).strftime('%Y-%m-%d %H:%M:%S')

    return sorted_arr, inicio_formatado, fim_formatado, total, algoritmo


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
            escrever.writerow(
                {'latitude': lat, 'longitude': lon, 'distancia': dist})

    print("Distâncias calculadas e salvas em fotos_com_distancia.csv")


def calc_tempo(alg, lista):
    inicio = time.time()
    alg(lista)
    fim = time.time()
    return fim - inicio


def comparar_dois(lista):
    especificacoes = especificacoes_do_sistema()

    metodos = [bubble_sort, insertion_sort, selection_sort,
               quick_sort, merge_sort, binary_insertion_sort, heap_sort, bucket_sort]

    met1, met2 = random.sample(metodos, 2)

    tempo1 = calc_tempo(met1, lista)
    tempo2 = calc_tempo(met2, lista)

    conexao = conectar_banco()
    cursor = conexao.cursor()

    criar_tabela(cursor)

    inserir_dados(cursor, especificacoes, met1.__name__, tempo1)
    inserir_dados(cursor, especificacoes, met2.__name__, tempo2)

    conexao.commit()

    print(f"Método 1: {met1.__name__}")
    print(f"Método 2: {met2.__name__}")

    print(
        f"Tempo de execução do método {met1.__name__}: {tempo1:.19f} segundos")
    print(
        f"Tempo de execução do método {met2.__name__}: {tempo2:.19f} segundos")

    if tempo1 < tempo2:
        print(f"O método {met1.__name__} foi mais rápido!")
    elif tempo1 > tempo2:
        print(f"O método {met2.__name__} foi mais rápido!")
    else:
        print("Ambos os algoritmos tiveram o mesmo tempo de execução!")


def resultado(algoritmo, inicio, fim, total):
    especificacoes = especificacoes_do_sistema()

    # Verifica se o arquivo existe para não repetir o cabeçalho
    arquivo_existe = os.path.isfile('arquivo_final.csv')

    with open('arquivo_final.csv', 'a', newline='', encoding='utf-8') as arquivo:
        colunas = [
            'Algoritmo', 'Inicio', 'Fim', 'Tempo Total', 'Sistema Operacional', 'Versao SO',
            'Nome Computador', 'Arquitetura', 'Processador', 'Cores Fisicos', 'Cores Logicos',
            'Frequencia CPU (MHz)', 'Memoria Total (GB)', 'Armazenamento Total (GB)',
            'Armazenamento Usado (GB)', 'Armazenamento Livre (GB)'
        ]

        escrever = csv.DictWriter(arquivo, fieldnames=colunas)

        # Escreve o cabeçalho apenas se o arquivo não existe
        if not arquivo_existe:
            escrever.writeheader()

        for alg, ini, fim_alg, tot in zip(algoritmo, inicio, fim, total):
            escrever.writerow({
                'Algoritmo': alg,
                'Inicio': ini,
                'Fim': fim_alg,
                'Tempo Total': tot,
                'Sistema Operacional': especificacoes["sistema_operacional"],
                'Versao SO': especificacoes["versao_so"],
                'Nome Computador': especificacoes["nome_computador"],
                'Arquitetura': especificacoes["arquitetura"],
                'Processador': especificacoes["processador"],
                'Cores Fisicos': especificacoes["cores_fisicos"],
                'Cores Logicos': especificacoes["cores_logicos"],
                'Frequencia CPU (MHz)': especificacoes["frequencia_cpu_mhz"],
                'Memoria Total (GB)': especificacoes["memoria_total_gb"],
                'Armazenamento Total (GB)': especificacoes["armazenamento_total_gb"],
                'Armazenamento Usado (GB)': especificacoes["armazenamento_usado_gb"],
                'Armazenamento Livre (GB)': especificacoes["armazenamento_livre_gb"]
            })


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


def limpartela():
    os.system("cls")


def especificacoes_do_sistema():
    especificacoes = {
        "sistema_operacional": platform.system(),
        "versao_so": platform.version(),
        "nome_computador": platform.node(),
        "arquitetura": platform.machine(),
        "processador": platform.processor(),
        "cores_fisicos": psutil.cpu_count(logical=False),
        "cores_logicos": psutil.cpu_count(logical=True),
        "frequencia_cpu_mhz": psutil.cpu_freq().current,
        "memoria_total_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "armazenamento_total_gb": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        "armazenamento_usado_gb": round(psutil.disk_usage('/').used / (1024 ** 3), 2),
        "armazenamento_livre_gb": round(psutil.disk_usage('/').free / (1024 ** 3), 2)
    }
    return especificacoes


def conexao():
    # Conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="192.168.10.138",
        user="kezio",
        password="kezio123",
        database="teste",
        allow_local_infile=True  # Permite o uso de LOCAL
    )

    cursor = conexao.cursor()

    # Criação da tabela com tipos de dados correspondentes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS algoritmos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        algoritmo VARCHAR(50),
        inicio DATETIME,
        fim DATETIME,
        tempo_total DOUBLE,
        sistema_operacional VARCHAR(50),
        versao_so VARCHAR(100),
        nome_computador VARCHAR(100),
        arquitetura VARCHAR(50),
        processador VARCHAR(100),
        cores_fisicos INT,
        cores_logicos INT,
        frequencia_cpu_mhz DOUBLE,
        memoria_total_gb DOUBLE,
        armazenamento_total_gb DOUBLE,
        armazenamento_usado_gb DOUBLE,
        armazenamento_livre_gb DOUBLE
    );
    ''')

    # Comando para importar o CSV com LOCAL
    comando_sql = """
    LOAD DATA LOCAL INFILE 'arquivo_final.csv'
    INTO TABLE algoritmos
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (algoritmo, inicio, fim, tempo_total, sistema_operacional, versao_so, nome_computador,
     arquitetura, processador, cores_fisicos, cores_logicos, frequencia_cpu_mhz, 
     memoria_total_gb, armazenamento_total_gb, armazenamento_usado_gb, armazenamento_livre_gb);
    """

    try:
        print("Executando comando SQL para importar dados...")
        cursor.execute(comando_sql)
        conexao.commit()
        print("Dados importados com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        # Fechando o cursor e a conexão
        cursor.close()
        conexao.close()

def conectar_banco():
    return mysql.connector.connect(
        host="192.168.10.138",
        user="kezio",
        password="kezio123",
        database="teste"
    )

# Função para criar a tabela no banco de dados, se não existir


def criar_tabela(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comparar2 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        algoritmo VARCHAR(50),
        tempo DOUBLE,
        sistema_operacional VARCHAR(50),
        versao_so VARCHAR(100),
        nome_computador VARCHAR(100),
        arquitetura VARCHAR(50),
        processador VARCHAR(100),
        cores_fisicos INT,
        cores_logicos INT,
        frequencia_cpu_mhz DOUBLE,
        memoria_total_gb DOUBLE,
        armazenamento_total_gb DOUBLE,
        armazenamento_usado_gb DOUBLE,
        armazenamento_livre_gb DOUBLE
    );
    """)

# Função para inserir dados no banco de dados


def inserir_dados(cursor, especificacoes, algoritmo, tempo):
    cursor.execute("""
    INSERT INTO comparar2 (
        algoritmo, tempo, sistema_operacional, versao_so, nome_computador, 
        arquitetura, processador, cores_fisicos, cores_logicos, frequencia_cpu_mhz,
        memoria_total_gb, armazenamento_total_gb, armazenamento_usado_gb, armazenamento_livre_gb
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        algoritmo,
        tempo,
        especificacoes["sistema_operacional"],
        especificacoes["versao_so"],
        especificacoes["nome_computador"],
        especificacoes["arquitetura"],
        especificacoes["processador"],
        especificacoes["cores_fisicos"],
        especificacoes["cores_logicos"],
        especificacoes["frequencia_cpu_mhz"],
        especificacoes["memoria_total_gb"],
        especificacoes["armazenamento_total_gb"],
        especificacoes["armazenamento_usado_gb"],
        especificacoes["armazenamento_livre_gb"]
    ))
