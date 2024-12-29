from gera_array import GeraArray

class HeapSort:
    def __init__(self):
        self.comparacoes = 0
        self.atribuicoes = 0
        self.tempo_execucao = 0

    def corrige_heap_descendo(self, H, i, n):
        maior = i
        filho_esq = 2 * i + 1
        filho_dir = 2 * i + 2

        # Comparar com o filho esquerdo
        if filho_esq < n and H[filho_esq] > H[maior]:
            maior = filho_esq

        # Comparar com o filho direito
        if filho_dir < n and H[filho_dir] > H[maior]:
            maior = filho_dir

        # Troca e recursão se necessário
        if maior != i:
            H[i], H[maior] = H[maior], H[i]
            self.corrige_heap_descendo(H, maior, n)

    def constroi_heap(self, H):
        n = len(H)
        for i in range(n // 2 - 1, -1, -1):
            self.corrige_heap_descendo(H, i, n)

    def heap_sort(self, A):
        n = len(A)
        self.constroi_heap(A)
        for i in range(n - 1, 0, -1):
            # Trocar o maior elemento com o último
            A[0], A[i] = A[i], A[0]
            # Corrigir a heap reduzida
            self.corrige_heap_descendo(A, 0, i)

arr = GeraArray()
heap_sort = HeapSort()
A = arr.array_aleatorio(10)
print(A)
heap_sort.heap_sort(A)
print(A)