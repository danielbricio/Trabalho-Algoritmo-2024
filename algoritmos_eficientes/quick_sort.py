import random

class QuickSort:
    def __init__(self):
        self.comparacoes = 0
        self.atribuicoes = 0
        self.tempo_execucao = 0

    def sort(self, A):
        self._quick_sort(A, 0, len(A) - 1)

    def _quick_sort(self, A, inicio, fim):
        if inicio < fim: #Verifica se o metodo ja fez todas a iterações necessárias
            self.comparacoes += 1
            p = random.randint(inicio, fim)
            self.atribuicoes += 1
            A[p], A[fim] = A[fim], A[p]
            self.atribuicoes += 3 #atribuição por tupla
            x = self.particiona(A, inicio, fim) #chama o metodo particiona e iguala o return a x
            self.atribuicoes += 1
            self._quick_sort(A, inicio, x-1) #chamada recursiva do metodo quicksort com o subvertor formado a esquerda do original
            self._quick_sort(A, x+1, fim) #chamada recursiva do metodo quicksort com o subvertor formado a direita do original

    def particiona(self, A, inicio, fim):
        pivo = A[random.randint(inicio, fim)] #define o pivô como o ultimo elemento do array
        self.atribuicoes += 1
        i = inicio #define o indice i
        self.atribuicoes += 1

        for j in range(inicio, fim): #loop para iterar o array
            self.comparacoes += 1 
            if A[j] <= pivo: #se o elemento da iteração for menor que o pivô
                self.comparacoes += 1
                A[i], A[j] = A[j], A[i] #então ele troca de lugar com o elemento do indice i
                self.atribuicoes += 3 # Troca de posições (3 atribuições com uso de tupla)
                i += 1 #incrementa o i
                self.atribuicoes += 1
                
        
        A[i], A[fim] = A[fim], A[i] #troca o elemento do indice i com o ultimo elemento do sub array.
        self.atribuicoes += 3 # Troca de posições (3 atribuições com uso de tupla)

        return i
    
    def resultados(self):
        return {
            'comparacoes': self.comparacoes,
            'atribuicoes': self.atribuicoes,
            'tempo_execucao': self.comparacoes + self.atribuicoes}
