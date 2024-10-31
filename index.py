import Alg_Ordenacao
import aleatorio
import os

algoritmos = ["bubble_sort","insertion_sort","selection_sort","merge_sort","quick_sort","shell_sort"]
a = [64, 34, 25, 12, 22, 11, 90]

def AlgAleatorio():
    num = aleatorio.numAleatorio()
    
    if(num == 1):
        os.system("cls")
        Alg_Ordenacao.bubble_sort(a)
        print("Array Original:", a)
        print (Alg_Ordenacao.bubble_sort(a.copy()))
        return print("O algoritmo selecionado foi o bubble sort")
    
    if(num == 2):
        os.system("cls")
        Alg_Ordenacao.insertion_sort(a)
        print("Array Original:", a)
        print (Alg_Ordenacao.insertion_sort(a.copy()))
        return print("O algoritmo selecionado foi o insertion sort")
    
    if(num == 3):
        os.system("cls")
        Alg_Ordenacao.selection_sort(a)
        print("Array Original:", a)
        print (Alg_Ordenacao.selection_sort(a.copy()))
        return print("O algoritmo selecionado foi o selection sort")
    
    if(num == 4):
        os.system("cls")
        Alg_Ordenacao.merge_sort(a)
        print("Array Original:", a)
        print (Alg_Ordenacao.merge_sort(a.copy()))
        return print("O algoritmo selecionado foi o merge sort")
    
    if(num == 5):
        os.system("cls")
        Alg_Ordenacao.quick_sort(a)
        print("Array Original:", a)
        print(Alg_Ordenacao.quick_sort(a.copy()))
        return print("O algoritmo selecionado foi o quick sort")
    
    if(num == 6):
        os.system("cls")
        Alg_Ordenacao.shell_sort(a)
        print("Array Original:", a)
        print (Alg_Ordenacao.shell_sort(a.copy()))
        return print("O algoritmo selecionado foi o shell sort")
    
AlgAleatorio()