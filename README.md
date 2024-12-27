## Sobre o Projeto

Este projeto foi desenvolvido como parte de um trabalho prático focado na implementação e análise de algoritmos de ordenação. O principal objetivo é compreender o funcionamento e as diferenças entre algoritmos de ordenação não-eficientes e eficientes, explorando tanto a teoria quanto a aplicação prática. 

### Algoritmos Implementados

Os algoritmos de ordenação estão divididos em dois grupos:

- **Não-eficientes**:
  - **BubbleSort**: Realiza a ordenação comparando pares consecutivos de elementos, trocando-os se estiverem fora de ordem. Requer várias passagens pelo conjunto de dados.
  - **InsertionSort**: Insere cada elemento na posição correta em uma lista parcialmente ordenada, repetindo o processo até que todos os elementos estejam ordenados.
  - **SelectionSort**: Seleciona repetidamente o menor elemento e o coloca na posição correta, varrendo a lista para encontrar o próximo menor.

- **Eficientes**:
  - **QuickSort**: Divide a sequência em subpartes com base em um elemento pivô, ordenando recursivamente essas divisões.
  - **HeapSort**: Baseado na estrutura de heap, remove repetidamente o maior elemento do heap e o adiciona à sequência ordenada.
  - **MergeSort**: Utiliza a abordagem de dividir para conquistar, separando a sequência em partes menores, ordenando cada uma e mesclando os resultados.

### Tipos de Dados

Os algoritmos serão testados com diferentes tipos de entradas de dados para avaliar sua performance em cenários variados:
- **Ordenados**: Dados já ordenados em ordem crescente.
- **Inversamente ordenados**: Dados em ordem decrescente.
- **Quase ordenados**: Dados que apresentam pequenos desvios da ordem crescente.
- **Aleatórios**: Dados dispostos sem qualquer padrão específico.

### Objetivos da Análise

A análise terá como foco principal:
- **Número de Comparações**: Quantidade de vezes que dois elementos são comparados durante a ordenação.
- **Número de Atribuições**: Quantidade de trocas ou movimentações de elementos realizadas.
- **Tempo de Execução**: Medição do tempo necessário para a conclusão de cada algoritmo.

### Resultados Esperados

Os resultados obtidos serão organizados em tabelas e gráficos para facilitar a visualização e comparação do desempenho dos algoritmos. Com base nesses dados, será possível:
- Comparar os algoritmos não-eficientes entre si.
- Comparar os algoritmos eficientes entre si.
- Analisar as diferenças entre algoritmos não-eficientes e eficientes em cenários variados.

Este projeto não apenas explora a implementação dos algoritmos, mas também busca desenvolver um entendimento mais profundo sobre como eles se comportam na prática, considerando diferentes cenários e entradas de dados.
