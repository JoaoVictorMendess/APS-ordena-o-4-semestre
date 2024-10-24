def busca_linear(lista, valor_procurado):
    for indice in range(len(lista)):
        if lista[indice] == valor_procurado:
            return indice 
    return -1 

lista = [10, 23, 45, 70, 11, 15]
valor_procurado = 70

resultado = busca_linear(lista, valor_procurado)

if resultado != -1:
    print(f"Valor encontrado no índice {resultado}")
else:
    print("Valor não encontrado na lista")