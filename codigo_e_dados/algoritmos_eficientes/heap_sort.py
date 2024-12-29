from gera_array import GeraArray
import time

class HeapSort:
    def __init__(self):
        self.comparacoes = 0
        self.atribuicoes = 0
        self.tempo_execucao = 0

    def sort(self, A):
        start_time = time.time()
        self._heap_sort(A)
        end_time = time.time()  # Fim da medição de tempo
        self.tempo_execucao = end_time - start_time

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
                maior = filho_esq
                self.comparacoes += 1  # Atualização de maior

        # Comparar com o filho direito
        if filho_dir < n:
            self.comparacoes += 1
            if H[filho_dir] > H[maior]:
                maior = filho_dir
                self.comparacoes += 1  # Atualização de maior

        # Troca e recursão se necessário
        if maior != i:
            self.comparacoes += 1
            H[i], H[maior] = H[maior], H[i]
            self.atribuicoes += 3 # Troca de posições (3 atribuições com uso de tupla)
            self.corrige_heap_descendo(H, maior, n)

    def constroi_heap(self, H):
        n = len(H)
        for i in range(n // 2 - 1, -1, -1):
            self.corrige_heap_descendo(H, i, n)

    def _heap_sort(self, A):
        n = len(A)
        self.constroi_heap(A)
        for i in range(n - 1, 0, -1):
            # Trocar o maior elemento com o último
            A[0], A[i] = A[i], A[0]
            self.atribuicoes += 3  # Troca de posições (3 atribuições com uso de tupla)
            # Corrigir a heap reduzida
            self.corrige_heap_descendo(A, 0, i)

    def resultados(self):
        return f'''
            comparacoes: {self.comparacoes}\n
            atribuicoes: {self.atribuicoes}\n
            tempo_execucao: {self.tempo_execucao}\n'''

arr = GeraArray()
heap_sort = HeapSort()
A = arr.array_aleatorio(1000000)
print(A)
heap_sort.sort(A)
print(A)
print(heap_sort.resultados())