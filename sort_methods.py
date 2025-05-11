class MetodosOrdenamiento:

    def sortByBubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

    def sort_bubble_optimized(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            intercambiado = False
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    intercambiado = True
            if not intercambiado:
                break
        return arreglo

    def insertion_sort(self, array):
        arreglo = array.copy()
        for i in range(1, len(arreglo)):
            clave = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > clave:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = clave
        return arreglo

    def shell_sort(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo

    def sort_selection(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n - 1):
            minimo = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[minimo]:  # ← aquí había un error: estaba comparando con arreglo[i]
                    minimo = j
            arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]
        return arreglo
