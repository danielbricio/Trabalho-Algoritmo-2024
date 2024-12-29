import pandas as pd
import matplotlib.pyplot as plt

def gerar_graficos_insertion_sort():
    """
    Gera gráficos de desempenho (tempo, comparações, atribuições) do Insertion Sort.
    """
    caminho_csv = "algoritmos_nao_eficientes/Insertion_Sort/resultados_insertion_sort_final.csv"
    df = pd.read_csv(caminho_csv)

    tipos = df["Tipo"].unique()
    for tipo in tipos:
        dados_tipo = df[df["Tipo"] == tipo]

        # Gráfico de Tempo de Execução
        plt.figure()
        plt.plot(dados_tipo["Tamanho"], dados_tipo["Tempo (s)"], marker="o", label="Tempo de Execução")
        plt.title(f"Insertion Sort - Tempo de Execução ({tipo})")
        plt.xlabel("Tamanho da Lista")
        plt.ylabel("Tempo (s)")
        plt.grid()
        plt.legend()
        plt.savefig(f"algoritmos_nao_eficientes/Insertion_Sort/grafico_tempo_{tipo.lower().replace(' ', '_')}.png")

        # Gráfico de Comparações
        plt.figure()
        plt.plot(dados_tipo["Tamanho"], dados_tipo["Comparações"], marker="o", label="Comparações")
        plt.title(f"Insertion Sort - Comparações ({tipo})")
        plt.xlabel("Tamanho da Lista")
        plt.ylabel("Número de Comparações")
        plt.grid()
        plt.legend()
        plt.savefig(f"algoritmos_nao_eficientes/Insertion_Sort/grafico_comparacoes_{tipo.lower().replace(' ', '_')}.png")

        # Gráfico de Atribuições
        plt.figure()
        plt.plot(dados_tipo["Tamanho"], dados_tipo["Atribuições"], marker="o", label="Atribuições")
        plt.title(f"Insertion Sort - Atribuições ({tipo})")
        plt.xlabel("Tamanho da Lista")
        plt.ylabel("Número de Atribuições")
        plt.grid()
        plt.legend()
        plt.savefig(f"algoritmos_nao_eficientes/Insertion_Sort/grafico_atribuicoes_{tipo.lower().replace(' ', '_')}.png")

    print("Gráficos gerados com sucesso!")

if __name__ == "__main__":
    gerar_graficos_insertion_sort()
