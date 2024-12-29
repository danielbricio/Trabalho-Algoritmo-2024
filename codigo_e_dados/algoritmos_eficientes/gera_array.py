import random

class GeraArray:
    def __init__(self):
        pass

    def array_ordenado_cresc(self, n):
        A = [i for i in range(n)]
        return A

    def array_ordenado_descr(self, n):
        A = [i for i in range(n-1, -1, -1)]
        return A

    def array_quase_ordenado(self, n):
        A = [i for i in range(n)]

        for _ in range(n // 10):  
            i, j = random.sample(range(n), 2)  
            A[i], A[j] = A[j], A[i]

        return A

    def array_aleatorio(self, n):
        A = []

        while len(A) < n:
            x = random.randint(0,100)
            if x not in A:
                A.append(x)

        return A