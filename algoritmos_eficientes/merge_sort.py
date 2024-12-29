class MergeSort:
    def __init__(self):
        self.comparacoes = 0
        self.atribuicoes = 0
        self.tempo_execucao = 0

    def sort(self, A):
        self._merge_sort(A, 0, len(A) - 1)

    def combina(self, A, inicio, meio, fim):
        n_um = meio - inicio + 1
        n_dois = fim - meio
        self.atribuicoes += 2

        B = [0] * n_um
        C = [0] * n_dois
        self.atribuicoes += 2

        for i in range(n_um):
            self.atribuicoes += 1 #atribuição a var i
            B[i] = A[inicio + i]
            self.atribuicoes += 1

        for j in range(n_dois):
            self.atribuicoes += 1 #atribuição a var i
            C[j] = A[meio + j + 1]
            self.atribuicoes += 1 

        i = 0
        j = 0
        k = inicio
        self.atribuicoes += 3
        
        while i < n_um and j < n_dois:
            self.comparacoes += 1
            if B[i] < C[j]:
                self.comparacoes += 1
                A[k] = B[i]
                i += 1
                self.atribuicoes += 2
            else:
                A[k] = C[j]
                j += 1
                self.atribuicoes += 2
            k += 1
            self.atribuicoes += 1

        while i < n_um:
            self.comparacoes += 1
            A[k] = B[i]
            i += 1
            k += 1
            self.atribuicoes += 3

        while j < n_dois:
            self.comparacoes += 1
            A[k] = C[j]
            j += 1
            k += 1
            self.atribuicoes += 3

    def _merge_sort(self, A, inicio, fim):
        if inicio < fim:
            self.comparacoes += 1
            meio = (inicio + fim) // 2
            self.atribuicoes += 1
            self._merge_sort(A, inicio, meio)
            self._merge_sort(A, meio + 1, fim)
            self.combina(A, inicio, meio, fim)

    def resultados(self):
        return {
            'comparacoes': self.comparacoes,
            'atribuicoes': self.atribuicoes,
            'tempo_execucao': self.comparacoes + self.atribuicoes}