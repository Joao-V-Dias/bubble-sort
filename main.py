import random

def generate_list(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(1, n))
    return lst

def bubble_sort(unsorted_list):
    lst = unsorted_list.copy()
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                aux = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = aux
    return lst

for size in [10, 100, 1000]:
    lst = generate_list(size)
    sorted_lst = bubble_sort(lst)

    print(f"\nLista gerada (tamanho {size}):")
    print(lst)

    print(f"Lista ordenada (tamanho {size}):")
    print(sorted_lst)