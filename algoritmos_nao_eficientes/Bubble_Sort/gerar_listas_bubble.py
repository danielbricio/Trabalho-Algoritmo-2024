import random

def gerar_listas(tamanho):
    """
    Gera diferentes tipos de listas para teste:
    - Ordenada
    - Inversamente ordenada
    - Quase ordenada (com 10% dos elementos fora de ordem)
    - Aleatória

    Argumentos:
    - tamanho (int): Tamanho das listas a serem geradas.

    Retorna:
    - tuple: Quatro listas:
        - ordenada (list): Lista com elementos em ordem crescente.
        - inversamente_ordenada (list): Lista com elementos em ordem decrescente.
        - quase_ordenada (list): Lista com 10% dos elementos fora de ordem.
        - aleatoria (list): Lista com elementos aleatórios.
    """
    if tamanho <= 0:
        raise ValueError("O tamanho da lista deve ser maior que zero.")

    # Lista ordenada
    ordenada = list(range(tamanho))

    # Lista inversamente ordenada
    inversamente_ordenada = list(range(tamanho, 0, -1))

    # Lista quase ordenada (troca 10% dos elementos aleatoriamente)
    quase_ordenada = ordenada[:]
    num_trocas = max(1, tamanho // 10)  # Garante ao menos uma troca, mesmo para tamanhos pequenos
    for _ in range(num_trocas):
        i, j = random.sample(range(tamanho), 2)
        quase_ordenada[i], quase_ordenada[j] = quase_ordenada[j], quase_ordenada[i]

    # Lista aleatória
    aleatoria = random.sample(range(tamanho * 10), tamanho)

    return ordenada, inversamente_ordenada, quase_ordenada, aleatoria
