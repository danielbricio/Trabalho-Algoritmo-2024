from gerar_dados import gerar_listas
import time

# Função BubbleSort para ordenar uma lista de números
def bubble_sort(arr):
    """
    Algoritmo BubbleSort:
    - Melhor caso (lista já ordenada): O(n)
    - Pior caso (lista inversamente ordenada): O(n^2)
    - Caso médio: O(n^2)

    Explicação:
    - No pior caso, cada elemento será comparado com todos os outros (n * (n-1) / 2 comparações).
    - No melhor caso, o loop interno não realiza trocas, otimizando o desempenho para O(n).
    """
    n = len(arr)
    comparacoes = 0  # Conta quantas comparações foram feitas
    trocas = 0  # Conta quantas trocas foram feitas

    # Loop externo para percorrer toda a lista
    for i in range(n):
        # Últimos i elementos já estão no lugar após cada iteração do loop externo
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                # Realiza a troca
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1

    return arr, comparacoes, trocas

# Teste inicial do BubbleSort com diferentes listas
if __name__ == "__main__":
    tamanhos = [10, 100, 1000, 10000]  # Podemos expandir para 100000 e 1000000, mas pode ser lento para o BubbleSort
    for tamanho in tamanhos:
        print(f"\n=== Testes com listas de tamanho {tamanho} ===")
        listas = gerar_listas(tamanho)
        nomes = ["Ordenada", "Inversamente Ordenada", "Quase Ordenada", "Aleatória"]

        for nome, lista in zip(nomes, listas):
            inicio = time.time()  # Início da medição de tempo
            resultado, comparacoes, trocas = bubble_sort(lista[:])  # Copiar lista para não alterar o original
            fim = time.time()  # Fim da medição de tempo
            print(f"\nLista {nome}:")
            print(f"Tamanho: {tamanho}")
            print(f"Comparações: {comparacoes}, Trocas: {trocas}")
            print(f"Tempo de execução: {fim - inicio:.6f} segundos")
