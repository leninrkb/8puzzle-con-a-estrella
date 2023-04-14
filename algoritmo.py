import copy
import numpy as np

global TABLERO
TABLERO = np.array([
    [0,1,2],
    [3,4,5],
    [6,7,8],
])

def calcular_euristica(tablero_nodo, tablero_solucion=TABLERO):
    euristica = 0
    x, y = tablero_solucion.shape
    for i in range(x):
        for j in range(y):
            if not tablero_nodo[i, j] == tablero_solucion[i, j]:
                euristica+=1
    return euristica

def nodo_por_expandir(lista_prioridad):
    fn = []
    for i in range(len(lista_prioridad)):
        fn.append(lista_prioridad[i].gn + lista_prioridad[i].hn)
    return min(fn)

def generar_estados(nodo):
    nodo_arriba = copy.deepcopy(nodo)
    nodo_abajo = copy.deepcopy(nodo)
    nodo_izquierda = copy.deepcopy(nodo)
    nodo_derecha = copy.deepcopy(nodo)
    nodos_generados = []
    if nodo_arriba.mover_arriba():
        nodo_arriba.accion = 'movio arriba'
        nodo_arriba.gn+=1
        nodo_arriba.hn = calcular_euristica(nodo_arriba.tablero)
        nodo_arriba.calcfn()
        nodos_generados.append(nodo_arriba)
    if nodo_abajo.mover_abajo():
        nodo_abajo.accion = 'movio abajo'
        nodo_abajo.gn+=1
        nodo_abajo.hn = calcular_euristica(nodo_abajo.tablero)
        nodo_abajo.calcfn()
        nodos_generados.append(nodo_abajo)
    if nodo_izquierda.mover_izquierda():
        nodo_izquierda.accion = 'movio izquierda'
        nodo_izquierda.gn+=1
        nodo_izquierda.hn = calcular_euristica(nodo_izquierda.tablero)
        nodo_izquierda.calcfn()
        nodos_generados.append(nodo_izquierda)
    if nodo_derecha.mover_derecha():
        nodo_derecha.accion = 'movio derecha'
        nodo_derecha.gn+=1
        nodo_derecha.hn = calcular_euristica(nodo_derecha.tablero)
        nodo_derecha.calcfn()
        nodos_generados.append(nodo_derecha)
    if len(nodos_generados) == 0:
        return None
    return nodos_generados



