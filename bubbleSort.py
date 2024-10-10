l = [7,8,10,5,4,1]

def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

resultado = bubbleSort(l)
print(resultado)

