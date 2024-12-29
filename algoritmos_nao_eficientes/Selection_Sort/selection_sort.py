# Implementacao do algoritmo SelectionSort
import time
import random
import csv


def selection_sort(arr):
    """
    Implementa o algoritmo SelectionSort.
    
    :param arr: Lista de inteiros a ser ordenada.
    :return: Lista ordenada.
    """
    n = len(arr)
    for i in range(n):
        # Encontra o menor elemento no restante da lista
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Troca o menor elemento com o primeiro elemento não ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Funcoes para gerar diferentes tipos de sequencias
def generate_ordered_sequence(size):
    return list(range(size))

def generate_reverse_ordered_sequence(size):
    return list(range(size, 0, -1))

def generate_almost_ordered_sequence(size):
    seq = list(range(size))
    # Introduz algumas desordens
    for _ in range(size // 10):
        i, j = random.sample(range(size), 2)
        seq[i], seq[j] = seq[j], seq[i]
    return seq

def generate_random_sequence(size):
    return random.sample(range(size * 2), size)

# Codigo principal para executar os testes
def main():
    sizes = [10, 100, 1000, 10000, 100000]  # Limita a 10.000 elementos
    test_cases = {
        "Ordered": generate_ordered_sequence,
        "Reverse Ordered": generate_reverse_ordered_sequence,
        "Almost Ordered": generate_almost_ordered_sequence,
        "Random": generate_random_sequence,
    }
    
    results = []

    for size in sizes:
        for case_name, generator in test_cases.items():
            arr = generator(size)
            start_time = time.time()
            selection_sort(arr)
            elapsed_time = time.time() - start_time
            
            results.append((size, case_name, elapsed_time))
            print(f"Tested {case_name} sequence with {size} elements in {elapsed_time:.6f} seconds.")
    
    # Salva os resultados em um arquivo CSV
    with open("selection_sort_results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Size", "Case", "Time (s)"])  # Cabeçalho
        writer.writerows(results)  # Dados

    return results

if __name__ == "__main__":
    main()