import algoritmo
from nodo import Nodo

nodo = Nodo()

nodos = algoritmo.generar_estados(nodo)
for nodo in nodos:
    print(nodo.tablero, end='\n')
    