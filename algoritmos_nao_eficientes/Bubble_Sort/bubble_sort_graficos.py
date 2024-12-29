import pandas as pd
import matplotlib.pyplot as plt

def gerar_graficos_bubble_sort():
    """
    Gera gráficos de desempenho (tempo, comparações, trocas) do BubbleSort
    com base nos resultados salvos em CSV.
    """
    caminho_base = "algoritmos_nao_eficientes/Bubble_Sort/"
    df = pd.read_csv(f"{caminho_base}resultados_bubble_sort_final.csv")

    # Altere "Trocas" para "Trocas (Atribuições)"
    col_trocas = "Trocas (Atribuições)"

    # Gráficos para cada tipo de lista
    tipos = df["Tipo"].unique()
    for tipo in tipos:
        dados_tipo = df[df["Tipo"] == tipo]

        # Gráfico de Tempo de Execução
        plt.figure()
        plt.plot(dados_tipo["Tamanho"], dados_tipo["Tempo (s)"], marker='o', label="Tempo de Execução")
        plt.title(f"BubbleSort - Tempo de Execução ({tipo})")
        plt.xlabel("Tamanho da Lista")
        plt.ylabel("Tempo (s)")
        plt.grid()
        plt.legend()
        plt.savefig(f"{caminho_base}grafico_tempo_{tipo.lower().replace(' ', '_')}.png")

        # Gráfico de Comparações
        plt.figure()
        plt.plot(dados_tipo["Tamanho"], dados_tipo["Comparações"], marker='o', label="Comparações")
        plt.title(f"BubbleSort - Comparações ({tipo})")
        plt.xlabel("Tamanho da Lista")
        plt.ylabel("Número de Comparações")
        plt.grid()
        plt.legend()
        plt.savefig(f"{caminho_base}grafico_comparacoes_{tipo.lower().replace(' ', '_')}.png")

        # Gráfico de Trocas
        plt.figure()
        plt.plot(dados_tipo["Tamanho"], dados_tipo[col_trocas], marker='o', label="Trocas (Atribuições)")
        plt.title(f"BubbleSort - Trocas ({tipo})")
        plt.xlabel("Tamanho da Lista")
        plt.ylabel("Número de Trocas")
        plt.grid()
        plt.legend()
        plt.savefig(f"{caminho_base}grafico_trocas_{tipo.lower().replace(' ', '_')}.png")

    print("Gráficos gerados com sucesso!")

if __name__ == "__main__":
    gerar_graficos_bubble_sort()