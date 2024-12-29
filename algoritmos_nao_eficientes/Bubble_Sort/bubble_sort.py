import sys
import os
import time
import pandas as pd

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from algoritmos_nao_eficientes.Bubble_Sort.gerar_listas_bubble import gerar_listas

# Função BubbleSort para ordenar uma lista de números
def bubble_sort(arr):
    """
    Algoritmo BubbleSort:
    - Melhor caso (lista já ordenada): O(n)
    - Pior caso (lista inversamente ordenada): O(n^2)
    - Caso médio: O(n^2)

    Descrição:
    - Compara elementos adjacentes em uma lista e os troca caso estejam fora de ordem.
    - Esse processo é repetido até que toda a lista esteja ordenada.

    Argumentos:
    - arr (list): Lista de números a ser ordenada.

    Retorna:
    - list: Lista ordenada.
    - int: Número de comparações realizadas.
    - int: Número de trocas realizadas.
    """
    n = len(arr)
    comparacoes = 0  # Conta o número de comparações realizadas
    trocas = 0  # Conta o número de trocas realizadas

    # Percorre a lista várias vezes
    for i in range(n):
        # Cada iteração posiciona o maior elemento restante na posição correta
        for j in range(0, n - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                # Realiza a troca entre os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1

    return arr, comparacoes, trocas


def executar_testes(tamanhos):
    """
    Executa testes do BubbleSort para diferentes tamanhos de listas e categorias de dados.
    Resultados são exibidos no console e exportados para um arquivo CSV na pasta "resultados".

    Argumentos:
    - tamanhos (list): Lista de tamanhos das listas a serem testadas.
    """
    resultados = []  # Lista para armazenar os resultados dos testes

    for tamanho in tamanhos:
        print(f"\n=== Testes com listas de tamanho {tamanho} ===")
        listas = gerar_listas(tamanho)  # Gera listas para os testes
        nomes = ["Ordenada", "Inversamente Ordenada", "Quase Ordenada", "Aleatória"]

        # Executa o BubbleSort para cada categoria de lista
        for nome, lista in zip(nomes, listas):
            inicio = time.time()  # Marca o início do tempo de execução
            _, comparacoes, trocas = bubble_sort(lista[:])  # Executa o BubbleSort
            fim = time.time()  # Marca o fim do tempo de execução
            tempo_execucao = fim - inicio
            custo_relativo = comparacoes + trocas  # Calcula o custo relativo

            print(f"\nLista {nome}:")
            print(f"Tamanho: {tamanho}")
            print(f"Comparações: {comparacoes}, Trocas: {trocas}")
            print(f"Custo Relativo: {custo_relativo}")
            print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

            # Adiciona os resultados à lista para exportação
            resultados.append({
                "Tamanho": tamanho,
                "Tipo": nome,
                "Comparações": comparacoes,
                "Trocas (Atribuições)": trocas,
                "Custo Relativo": custo_relativo,
                "Tempo (s)": tempo_execucao,
            })

    # Exporta os resultados para um arquivo CSV na pasta "Bubble_Sort"
    os.makedirs(os.path.join("algoritmos_nao_eficientes", "Bubble_Sort"), exist_ok=True)
    caminho_arquivo = os.path.join("algoritmos_nao_eficientes", "Bubble_Sort", "resultados_bubble_sort_final.csv")
    df = pd.DataFrame(resultados)
    df.to_csv(caminho_arquivo, index=False)
    print(f"\nResultados salvos em '{caminho_arquivo}' \n")


if __name__ == "__main__":
    tamanhos = [10, 100, 1000, 10000]  # Define os tamanhos das listas para os testes
    executar_testes(tamanhos)
