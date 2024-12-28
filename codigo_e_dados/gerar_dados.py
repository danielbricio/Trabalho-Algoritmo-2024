import random

def gerar_listas(tamanho):
    """
    Gera diferentes tipos de listas para teste:
    - Ordenada
    - Inversamente ordenada
    - Quase ordenada (com 10% dos elementos fora de ordem)
    - Aleatória
    """
    # Lista ordenada
    ordenada = list(range(tamanho))

    # Lista inversamente ordenada
    inversamente_ordenada = list(range(tamanho, 0, -1))

    # Lista quase ordenada (troca 10% dos elementos aleatoriamente)
    quase_ordenada = ordenada[:]
    for _ in range(tamanho // 10):  # Trocar 10% dos elementos
        i, j = random.sample(range(tamanho), 2)
        quase_ordenada[i], quase_ordenada[j] = quase_ordenada[j], quase_ordenada[i]

    # Lista aleatória
    aleatoria = random.sample(range(tamanho), tamanho)

    return ordenada, inversamente_ordenada, quase_ordenada, aleatoria

if __name__ == "__main__":
    tamanho = 10
    listas = gerar_listas(tamanho)
    nomes = ["Ordenada", "Inversamente Ordenada", "Quase Ordenada", "Aleatória"]

    for nome, lista in zip(nomes, listas):
        print(f"{nome}: {lista}")
