import random
import time
from sort_methods import MetodosOrdenamiento
class Benchmarking:
    def __init__(self):
        print('Bench Inicializado')
    def ejemplo(self): 
        self.metodosOrdenamiento = MetodosOrdenamiento()
        arreglo = self.build_arreglo(100000)
        tarea = lambda: self.metodosOrdenamiento.sortByBubble(arreglo)
        timeMillis = self.contar_con_current_time_milles(tarea)
        timeNano = self.contar_con_nano_time(tarea)
        #ordena = self.sort_selection(tarea)

        print(f'Tiempo {timeMillis}')
        print(f'Tiempo {timeNano}')

    
    def build_arreglo(self, size):
        array = []
        for i in range(size):
            numero = random.randint(0,99999)
            array.append(numero)
        return array
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio)/1000000000
    
    
    def medir_tiempo(self,tarea, array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin - inicio
    

