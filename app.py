import algoritmo
from nodo import Nodo

nodo = Nodo()
nodo.hn = algoritmo.calcular_euristica(nodo.tablero)
nodo.calcfn()
nodo.imprimir_nodo()

lista_prioridad = algoritmo.generar_estados(nodo)
for n in lista_prioridad:
    n.imprimir_nodo()
    