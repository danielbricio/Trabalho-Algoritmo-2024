from insertion_sort import insertion_sort
from algoritmos_nao_eficientes.Insertion_Sort.gerar_listas_insertion import gerar_listas
import pandas as pd
import os
import time

def executar_testes_insertion_sort(tamanhos):
    """
    Executa testes do Insertion Sort para diferentes tamanhos de listas e categorias de dados.
    Resultados são exibidos no console e exportados para um arquivo CSV.
    """
    resultados = []
    tipos = ["Ordenada", "Inversamente Ordenada", "Quase Ordenada", "Aleatória"]

    for tamanho in tamanhos:
        print(f"\n=== Testes com listas de tamanho {tamanho} ===")
        listas = gerar_listas(tamanho)

        for tipo, lista in zip(tipos, listas):
            inicio = time.time()
            _, comparacoes, atribuicoes = insertion_sort(lista[:])
            fim = time.time()

            tempo_execucao = fim - inicio
            resultados.append({
                "Tamanho": tamanho,
                "Tipo": tipo,
                "Comparações": comparacoes,
                "Atribuições": atribuicoes,
                "Tempo (s)": tempo_execucao
            })
            print(f"Tipo: {tipo}, Tamanho: {tamanho}, Comparações: {comparacoes}, Atribuições: {atribuicoes}, Tempo: {tempo_execucao:.6f}s")

    # Salvar resultados em um CSV na pasta correta
    caminho_arquivo = "algoritmos_nao_eficientes/Insertion_Sort/resultados_insertion_sort_final.csv"
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    pd.DataFrame(resultados).to_csv(caminho_arquivo, index=False)
    print(f"\nResultados salvos em: {caminho_arquivo}")

if __name__ == "__main__":
    tamanhos = [10, 100, 1000, 10000]
    executar_testes_insertion_sort(tamanhos)
