class HeapSort:
    def __init__(self):
        self.comparacoes = 0
        self.atribuicoes = 0
        self.tempo_execucao = 0

    def sort(self, A):
        self._heap_sort(A)

    def corrige_heap_descendo(self, H, i, n):
        maior = i
        self.atribuicoes += 1  # Atribuição inicial de maior
        filho_esq = 2 * i + 1
        self.atribuicoes += 1  # Cálculo do filho esquerdo
        filho_dir = 2 * i + 2
        self.atribuicoes += 1  # Cálculo do filho direito

        # Comparar com o filho esquerdo
        if filho_esq < n:
            self.comparacoes += 1
            if H[filho_esq] > H[maior]:
                self.comparacoes += 1  # Atualização de maior
                maior = filho_esq
                self.atribuicoes += 1  #atribuição

        # Comparar com o filho direito
        if filho_dir < n:
            self.comparacoes += 1
            if H[filho_dir] > H[maior]:
                self.comparacoes += 1  # Atualização de maior
                maior = filho_dir
                self.atribuicoes += 1  #atribuição

        # Troca e recursão se necessário
        if maior != i:
            self.comparacoes += 1
            H[i], H[maior] = H[maior], H[i]
            self.atribuicoes += 3 # Troca de posições (3 atribuições com uso de tupla)
            self.corrige_heap_descendo(H, maior, n)

    def constroi_heap(self, H):
        n = len(H)
        self.atribuicoes +=1
        for i in range(n // 2 - 1, -1, -1):
            self.atribuicoes += 1
            self.corrige_heap_descendo(H, i, n)

    def _heap_sort(self, A):
        n = len(A)
        self.atribuicoes +=1
        self.constroi_heap(A)
        for i in range(n - 1, 0, -1):
            self.atribuicoes += 1
            # Trocar o maior elemento com o último
            A[0], A[i] = A[i], A[0]
            self.atribuicoes += 3  # Troca de posições (3 atribuições com uso de tupla)
            # Corrigir a heap reduzida
            self.corrige_heap_descendo(A, 0, i)

    def resultados(self):
        return {
            'comparacoes': self.comparacoes,
            'atribuicoes': self.atribuicoes,
            'tempo_execucao': self.comparacoes + self.atribuicoes}