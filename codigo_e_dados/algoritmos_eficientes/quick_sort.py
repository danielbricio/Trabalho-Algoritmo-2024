import time
from gera_array import GeraArray
string = "---------------------------------------//--------------------------------------------------"

class QuickSort:
    def __init__(self):
        self.comparacoes = 0
        self.atribuicoes = 0
        self.tempo_execucao = 0

    def sort(self, A):
        start_time = time.time()  # Início da medição de tempo
        self._quick_sort(A, 0, len(A) - 1)
        end_time = time.time()  # Fim da medição de tempo
        self.tempo_execucao = end_time - start_time

    def _quick_sort(self, A, inicio, fim):
        if inicio < fim: #Verifica se o metodo ja fez todas a iterações necessárias
            self.comparacoes += 1
            x = self.particiona(A, inicio, fim) #chama o metodo particiona e iguala o return a x
            self._quick_sort(A, inicio, x-1) #chamada recursiva do metodo quicksort com o subvertor formado a esquerda do original
            self._quick_sort(A, x+1, fim) #chamada recursiva do metodo quicksort com o subvertor formado a direita do original

    def particiona(self, A, inicio, fim):
        pivo = A[fim] #define o pivô como o ultimo elemento do array
        self.atribuicoes += 1
        i = inicio #define o indice i
        self.atribuicoes += 1

        for j in range(inicio, fim): #loop para iterar o array
            self.comparacoes += 1 
            if A[j] <= pivo: #se o elemento da iteração for menor que o pivô
                self.comparacoes += 1
                A[i], A[j] = A[j], A[i] #então ele troca de lugar com o elemento do indice i
                self.atribuicoes += 2
                i += 1 #incrementa o i
                self.atribuicoes += 1
        
        A[i], A[fim] = A[fim], A[i] #troca o elemento do indice i com o ultimo elemento do sub array.
        self.atribuicoes += 2

        return i
    
    def resultados(self):
        return f'''
            comparacoes: {self.comparacoes}\n
            atribuicoes: {self.atribuicoes}\n
            tempo_execucao: {self.tempo_execucao}\n'''

if __name__ == "__main__":
    arr = GeraArray()
    quicksort = QuickSort()
    A = arr.array_aleatorio(10)
    print(A)
    quicksort.sort(A)
    print(A)
    print(quicksort.resultados())
