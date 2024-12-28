import matplotlib.pyplot as plt
import pandas as pd

# Dados de exemplo (adicione valores reais após os testes)
tamanhos = [10, 100, 1000, 10000, 100000, 1000000]

# Tempos para diferentes tipos de listas
tempos_ordenada = [0.000000, 0.001069, 0.026037, 2.704760, 27.047600, 270.476000]
tempos_inversamente_ordenada = [0.000000, 0.000000, 0.053239, 5.926987, 59.269870, 592.698700]
tempos_quase_ordenada = [0.000000, 0.000000, 0.030401, 3.157323, 31.573230, 315.732300]
tempos_aleatoria = [0.000000, 0.000000, 0.045744, 4.499063, 44.990630, 449.906300]

# Criar um DataFrame para organizar os dados
df = pd.DataFrame({
    'Tamanho': tamanhos,
    'Ordenada': tempos_ordenada,
    'Inversamente Ordenada': tempos_inversamente_ordenada,
    'Quase Ordenada': tempos_quase_ordenada,
    'Aleatória': tempos_aleatoria,
})

# Gerar um gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(df['Tamanho'], df['Ordenada'], label='Ordenada', marker='o')
plt.plot(df['Tamanho'], df['Inversamente Ordenada'], label='Inversamente Ordenada', marker='o')
plt.plot(df['Tamanho'], df['Quase Ordenada'], label='Quase Ordenada', marker='o')
plt.plot(df['Tamanho'], df['Aleatória'], label='Aleatória', marker='o')

# Adicionar título e legendas
plt.title('Tempo de Execução do BubbleSort', fontsize=14)
plt.xlabel('Tamanho da Lista', fontsize=12)
plt.ylabel('Tempo (segundos)', fontsize=12)
plt.legend()
plt.grid()

# Salvar o gráfico
plt.savefig('grafico_bubblesort_completo.png')
plt.show()


# Salvar os dados em CSV
df.to_csv('resultados/resultados_bubble_sort_completo.csv', index=False)