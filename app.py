from benchmarking import Benchmarking
from sort_methods import MetodosOrdenamiento
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    metodos = MetodosOrdenamiento()
    benchmark = Benchmarking()

    # Tamaños a probar
    tamanios = [5000, 10000, 30000, 50000, 100000]
    tam_max = max(tamanios)

    arreglo_base = benchmark.build_arreglo(tam_max)

    # Diccionario de métodos 
    metodos_dict = {
        "burbuja": metodos.sortByBubble,
        "burbuja_mejorado": metodos.sort_bubble_optimized,
        "seleccion": metodos.sort_selection,
        "insersion": metodos.insertion_sort,
        "shell": metodos.shell_sort
    }
    
    resultados = [] 
    tiempos_by_metodo = {
        "burbuja": [],
        "burbuja_mejorado": [],
        "seleccion": [],
        "insersion": [],  
        "shell": []
    }

    for tam in tamanios:
        arreglo_actual = arreglo_base[:tam]
        for nombre, metodo in metodos_dict.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_actual.copy())
            resultados.append((tam, nombre, tiempo))
            tiempos_by_metodo[nombre].append((tam, tiempo))
            
    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")

    # Crear una nueva figura para la gráfica
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Configurar estilos y colores
    colors = {
        'burbuja': 'red',
        'burbuja_mejorado': 'orange',
        'seleccion': 'green',
        'insersion': 'blue',
        'shell': 'purple'
    }
    
    # Notaciones Big-O para la leyenda
    notations = {
        'burbuja': 'O(n²)',
        'burbuja_mejorado': 'O(n²)',
        'seleccion': 'O(n²)',
        'insersion': 'O(n²)',
        'shell': 'O(n log n)'
    }
    
    # Graficar cada método
    for metodo in tiempos_by_metodo:
        tamanios = [x[0] for x in tiempos_by_metodo[metodo]]
        tiempos = [x[1] for x in tiempos_by_metodo[metodo]]
        ax.plot(tamanios, tiempos, 
               label=f"{metodo} {notations[metodo]}", 
               marker='o', 
               color=colors[metodo],
               linewidth=2)
    
    # Configuración de la gráfica
    ax.set_title('Comparación de Algoritmos de Ordenamiento', fontsize=16)
    ax.set_xlabel('Tamaño del Arreglo', fontsize=14)
    ax.set_ylabel('Tiempo de Ejecución (segundos)', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(fontsize=12)
    ax.set_xticks(tamanios)
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    # Ajustar layout y guardar la gráfica
    plt.tight_layout()
    
    # Guardar la gráfica antes de mostrarla
    plt.savefig('comparacion_algoritmos.png', dpi=300, bbox_inches='tight')
    
    # Mostrar la gráfica (esto debe ir al final)
    plt.show()