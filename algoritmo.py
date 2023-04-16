import copy
import numpy as np
import logging
# from numba import njit

logging.basicConfig(filename='resultado.log', level=logging.INFO, filemode='w', format='%(levelname)s:%(name)s:\n%(message)s')
global TABLERO
TABLERO = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]
)

def calcular_heuristica(tablero, tablero_solucion=TABLERO):
    listanormal = tablero.flatten().tolist()
    listasolucion = tablero_solucion.flatten().tolist()
    heuristica = 0
    for index in range(len(listanormal)):
        if not listanormal[index] == listasolucion[index]:
            heuristica+=1

        # indicesolucion = listasolucion.index(listanormal[index])
        # hheuristica+= abs(index-indicesolucion)
    return heuristica

def es_solucion(lista_nodos):
    for nodo in lista_nodos:
        if nodo.hn == 0:
            resp = imprimir_camino(nodo, [])
            resp.reverse()
            for nodo in resp:
                logging.info(nodo.tablero)
            return True
    return False

def nodo_por_expandir(lista_prioridad):
    fns = []
    for index, nodo in enumerate(lista_prioridad):
        if nodo.estado == 'expandido':
            continue
        fns.append((index, nodo.fn, nodo))
    item = min(fns, key=lambda fns: fns[1])
    lista_prioridad.pop(item[0])
    nodo = item[2]
    nodo.estado = 'expandido'
    return nodo

def agregar_nodos(lista_prioridad, nuevos_nodos):
    for nodo in nuevos_nodos:
        # if controlar_repetido(lista_prioridad, nodo):
        #     continue
        lista_prioridad.append(nodo)

def controlar_repetido(lista_prioridad, nodo):
    for index, nodo in enumerate(lista_prioridad):
        nodot = lista_prioridad[index].tablero
        if np.array_equal(nodo, nodot):
            return True
    return False

def generar_estados(nodo):
    nodo_arriba = copy.deepcopy(nodo)
    nodo_abajo = copy.deepcopy(nodo)
    nodo_izquierda = copy.deepcopy(nodo)
    nodo_derecha = copy.deepcopy(nodo)
    nodos_generados = []
    if nodo_arriba.mover_arriba():
        nodo_arriba.accion = "movio arriba"
        nodo_arriba.estado = ''
        nodo_arriba.gn += 1
        nodo_arriba.hn = calcular_heuristica(nodo_arriba.tablero)
        nodo_arriba.calcfn()
        nodo_arriba.padre = nodo
        nodos_generados.append(nodo_arriba)
    if nodo_abajo.mover_abajo():
        nodo_abajo.accion = "movio abajo"
        nodo_abajo.estado = ''
        nodo_abajo.gn += 1
        nodo_abajo.hn = calcular_heuristica(nodo_abajo.tablero)
        nodo_abajo.calcfn()
        nodo_abajo.padre = nodo
        nodos_generados.append(nodo_abajo)
    if nodo_izquierda.mover_izquierda():
        nodo_izquierda.accion = "movio izquierda"
        nodo_izquierda.estado = ''
        nodo_izquierda.gn += 1
        nodo_izquierda.hn = calcular_heuristica(nodo_izquierda.tablero)
        nodo_izquierda.calcfn()
        nodo_izquierda.padre = nodo
        nodos_generados.append(nodo_izquierda)
    if nodo_derecha.mover_derecha():
        nodo_derecha.accion = "movio derecha"
        nodo_derecha.estado = ''
        nodo_derecha.gn += 1
        nodo_derecha.hn = calcular_heuristica(nodo_derecha.tablero)
        nodo_derecha.calcfn()
        nodo_derecha.padre = nodo
        nodos_generados.append(nodo_derecha)
    if len(nodos_generados) == 0:
        return None
    return nodos_generados


def es_solucionable(tablero):
    # Convertir la lista del estado inicial en una cadena
    estado_str = "".join(str(x) for x in tablero)
    # Contar el número de inversiones en la cadena
    inversiones = sum( 1 for i in range(8) for j in range(i + 1, 9) if estado_str[i] > estado_str[j] and estado_str[i] != "0" )
    # Comprobar si el número de inversiones es par o impar
    return inversiones % 2 == 0

def imprimir_camino(nodo, lista_respuesta):
    if nodo == None:
        return lista_respuesta
    # print(f'{nodo.tablero} \n')
    lista_respuesta.append(nodo)
    # logging.info(nodo.tablero)
    return imprimir_camino(nodo.padre, lista_respuesta)