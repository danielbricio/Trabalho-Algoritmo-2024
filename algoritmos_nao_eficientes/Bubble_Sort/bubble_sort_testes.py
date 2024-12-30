from bubble_sort import bubble_sort
from algoritmos_nao_eficientes.Bubble_Sort.gerar_listas_bubble import gerar_listas
from algoritmos_eficientes.main import grafico_array
import pandas as pd
import os
import time

def executar_testes_bubble_sort(tamanhos):
    """
    Executa testes do BubbleSort para diferentes tamanhos de listas e categorias de dados.
    Resultados são exibidos no console e exportados para um arquivo CSV na pasta correta.
    """
    resultados = []  # Lista para armazenar os resultados dos testes
    nomes = ["Ordenada", "Inversamente Ordenada", "Quase Ordenada", "Aleatória"]

    for tamanho in tamanhos:
        print(f"\n=== Testes com listas de tamanho {tamanho} ===")
        listas = gerar_listas(tamanho)  # Gera listas para os testes

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

            resultados.append({
                "Tamanho": tamanho,
                "Tipo": nome,
                "Comparações": comparacoes,
                "Trocas (Atribuições)": trocas,
                "Custo Relativo": custo_relativo,  # Soma das operações
                "Tempo (s)": tempo_execucao
            })

    # Ajustando o caminho para salvar o arquivo CSV
    caminho_arquivo = "algoritmos_nao_eficientes/Bubble_Sort/resultados_bubble_sort_testes.csv"
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    pd.DataFrame(resultados).to_csv(caminho_arquivo, index=False)
    print(f"\nResultados salvos em '{caminho_arquivo}' \n")

if __name__ == "__main__":
    tamanhos = [10, 100, 1000, 10000]
    executar_testes_bubble_sort(tamanhos)
