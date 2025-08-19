import time
import data

def bubble_sort(lst):
    start_time = time.perf_counter()
    n = len(lst)
    cont = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                aux = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = aux
                swapped = True
            cont += 1
        if swapped == False:
            break
    execution_time = time.perf_counter() - start_time
    print(f"-> Tempo: {execution_time:.5f} segundos")
    print(f"-> Quantidade de iteracoes: {cont}")
    return lst

print("Bubble Sort Otimizado")

for i in range(3):

    lst = data.lstInput[i]
    print(f"-> Lista {i + 1}: {lst}")
    lst = bubble_sort(lst)
    print(f"-> Lista {i + 1}: {lst} \n\n")
