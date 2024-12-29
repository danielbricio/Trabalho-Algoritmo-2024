import matplotlib.pyplot as plt

def plot_results(results):
    """
    Gera um gráfico comparando os tempos de execução do SelectionSort para diferentes tipos de sequências.

    :param results: Lista de tuplas no formato (tamanho, tipo_sequencia, tempo_execucao).
    """
    # Organiza os resultados por tipo de sequência
    sorted_results = {}
    for size, case_name, elapsed_time in results:
        if case_name not in sorted_results:
            sorted_results[case_name] = []
        sorted_results[case_name].append((size, elapsed_time))

    # Plota os resultados
    plt.figure(figsize=(10, 6))
    for case_name, data in sorted_results.items():
        data.sort()  # Ordena por tamanho
        sizes, times = zip(*data)
        plt.plot(sizes, times, marker='o', label=case_name)

    plt.title("Tempo de Execução do SelectionSort")
    plt.xlabel("Tamanho da Sequência")
    plt.ylabel("Tempo de Execução (segundos)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de como chamar a funcao plot_results
def main():
    # Simula resultados para teste
    results = [
        (10, "Ordered", 0.001),
        (100, "Ordered", 0.005),
        (1000, "Ordered", 0.05),
        (10, "Random", 0.002),
        (100, "Random", 0.01),
        (1000, "Random", 0.07),
    ]
    plot_results(results)

if __name__ == "__main__":
    main()
