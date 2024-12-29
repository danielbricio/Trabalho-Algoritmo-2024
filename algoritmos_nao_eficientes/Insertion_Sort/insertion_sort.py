import time
import csv

def insertion_sort(arr):
    """
    Ordena uma lista usando o algoritmo Insertion Sort.

    Parâmetros:
        arr (list): Lista de números a ser ordenada.

    Retorna:
        tuple: Lista ordenada, número de comparações e número de atribuições.
    """
    comparacoes = 0  # Contador de comparações realizadas no algoritmo
    atribuicoes = 0  # Contador de atribuições realizadas no algoritmo

    for i in range(1, len(arr)):
        key = arr[i]  # Elemento a ser inserido na posição correta
        j = i - 1
        atribuicoes += 1  # Atribuição ao definir key

        # Move os elementos que são maiores que 'key' para uma posição à frente
        while j >= 0 and arr[j] > key:
            comparacoes += 1  # Contabiliza a comparação no while
            arr[j + 1] = arr[j]
            atribuicoes += 1  # Move o elemento para frente
            j -= 1

        if j >= 0:  # Contabiliza a última comparação que falhou no while
            comparacoes += 1

        arr[j + 1] = key  # Insere o 'key' na posição correta
        atribuicoes += 1

    return arr, comparacoes, atribuicoes

if __name__ == "__main__":
    import random

    tamanhos = [10, 100, 1000, 10000]  # Ajustar para limitar a 10 mil elementos
    tipos = ["Ordenada", "Inversamente Ordenada", "Quase Ordenada", "Aleatória"]
    resultados = []  # Lista para armazenar os resultados para gráficos

    for tamanho in tamanhos:
        for tipo in tipos:
            if tipo == "Ordenada":
                array = list(range(tamanho))
            elif tipo == "Inversamente Ordenada":
                array = list(range(tamanho, 0, -1))
            elif tipo == "Quase Ordenada":
                array = list(range(tamanho))
                for _ in range(tamanho // 10):
                    i, j = random.sample(range(tamanho), 2)
                    array[i], array[j] = array[j], array[i]
            elif tipo == "Aleatória":
                array = random.sample(range(tamanho * 10), tamanho)

            print(f"\nTamanho: {tamanho}, Tipo: {tipo}")
            print(f"Array antes da ordenação: {array[:10]}...")

            inicio = time.time()
            ordenado, comparacoes, atribuicoes = insertion_sort(array)
            fim = time.time()

            print(f"Array depois da ordenação: {ordenado[:10]}...")
            print(f"Comparações: {comparacoes}, Atribuicoes: {atribuicoes}, Tempo: {fim - inicio:.6f} segundos")

            # Armazena os resultados para análise posterior
            resultados.append({
                "Tamanho": tamanho,
                "Tipo": tipo,
                "Comparações": comparacoes,
                "Atribuições": atribuicoes,
                "Tempo": fim - inicio
            })

    # Exportar resultados para um arquivo CSV
    with open("resultados/insertion_sort_resultados.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Tamanho", "Tipo", "Comparações", "Atribuições", "Tempo"])
        writer.writeheader()
        writer.writerows(resultados)

    print("Resultados salvos em 'resultados/insertion_sort_resultados.csv'.")