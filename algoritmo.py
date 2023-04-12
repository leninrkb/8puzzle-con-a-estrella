import copy

def calcular_euristica(tablero_solucion, tablero_nodo):
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
    nodo_arriba = copy.copy(nodo)
    nodo_abajo = copy.copy(nodo)
    nodo_izquierda = copy.copy(nodo)
    nodo_derecha = copy.copy(nodo)
    nodos_generados = []
    if nodo_arriba.mover_arriba():
        nodos_generados.append(nodo_arriba)
    if nodo_abajo.mover_abajo():
        nodos_generados.append(nodo_abajo)
    if nodo_izquierda.mover_izquierda():
        nodos_generados.append(nodo_izquierda)
    if nodo_derecha.mover_derecha():
        nodos_generados.append(nodo_derecha)
    if len(nodos_generados) == 0:
        return None
    return nodos_generados



