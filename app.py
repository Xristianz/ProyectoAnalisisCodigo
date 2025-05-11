from benchmarking import Benchmarking
from sort_methods import MetodosOrdenamiento

if __name__ == "__main__":
   
    metodos = MetodosOrdenamiento()
    benchmark = Benchmarking()

    #Tamaños a probar
    tamanios = [5000,10000,30000,50000,100000]
    tam_max = max(tamanios)

    arreglo_base = benchmark.build_arreglo(tam_max)

    #Diccionario de metodos 
    metodos = {
        "Burbuja" : metodos.sortByBubble,
        "Burbuja Mejorado": metodos.sort_bubble_optimized,
        "Seleccion": metodos.sort_selection,
        "Insersion": metodos.insertion_sort,
        "Shell": metodos.shell_sort
    }
    
    resultados = [] 

    for tam in tamanios:
        arreglo_actual = arreglo_base[:tam]
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_actual.copy())
            tupla_resultado = ( tam, nombre, tiempo)
            resultados.append(tupla_resultado)

    for resultado in resultados:
        tam, nombre,tiempo = resultado
        print(f"Tamaño: {tam}, Metodo: {nombre}, Tiempo: {tiempo: 6f} segundos ")

        tiempos_by_metodo={
        "burbuja": [],
        "burbuja_mejorado": [],
        "seleccion" : [],
        "shell": [],
        }