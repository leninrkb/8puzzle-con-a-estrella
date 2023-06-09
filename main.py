import algoritmo
from  memory_profiler import profile
from nodo import Nodo
import time

nodo = Nodo()
# nodo.facil()
# nodo.medio()
# nodo.dificil()

nodo.hn = algoritmo.calcular_heuristica(nodo.tablero)
nodo.calcfn()
nodo.imprimir_nodo()

lista_prioridad = []
nuevos_nodos = algoritmo.generar_estados(nodo)
algoritmo.agregar_nodos( lista_prioridad, nuevos_nodos)

@profile(stream=open('memory_profile.log', 'w+'))
def inicio():
    tinicio = time.time()
    while True:
        nodo = algoritmo.nodo_por_expandir(lista_prioridad)
        nodo.imprimir_nodo()
        # time.sleep(1)
        nuevos_nodos = algoritmo.generar_estados(nodo)
        if algoritmo.es_solucion(nuevos_nodos): 
            break;
        algoritmo.agregar_nodos(lista_prioridad, nuevos_nodos)
        print('nodos: ',len(lista_prioridad))
    tfin = time.time()
    tt = tfin - tinicio
    min = tt//60
    seg = tt % 60
    print(f'se encontro solucion, tiempo: {min} min : {seg} seg')
inicio()

