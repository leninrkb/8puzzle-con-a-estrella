import numpy as np
from random import shuffle

class Nodo:
    def __init__(self):
        self.tablero = np.array([
             [2, 3, 6],
            [0, 4, 8],
            [1, 7, 5]
        ])
        self.padre = None
        self.gn = 0 #costo camino
        self.hn = 0 #euristica
        self.fn = 0 #costo total
        self.accion = 'tablero inicial'
        self.estado = ''

    def calcfn(self):
        self.fn = self.gn + self.hn

    def facil(self):
        self.tablero = np.array([
            [4, 1, 3],
            [2, 8, 5],
            [0, 7, 6],
        ])
    def medio(self):
        self.tablero = np.array([
            [4, 8, 1],
            [2, 6, 3],
            [7, 5, 0],
        ])
    def dificil(self):
        self.tablero = np.array([
            [2, 4, 1],
            [8, 3, 0],
            [7, 6, 5],
        ])
    def llamen_a_dios(self):
        self.tablero = np.array([
            [1, 5, 6],
            [4, 8, 2],
            [7, 0, 3],
        ])

    def mezclar_tablero(self):
        flat_puzzle = self.tablero.flatten().tolist()
        shuffle(flat_puzzle)
        shuffled_puzzle = np.array(flat_puzzle).reshape(self.tablero.shape)
        self.tablero = shuffled_puzzle

    def poscicion_cero(self):
        x, y = self.tablero.shape
        for i in range(x):
            for j in range(y):
                if self.tablero[i, j] == 0:
                    return (i, j)
    def mover_arriba(self):
        x, y = self.poscicion_cero()
        if x-1 >= 0:
            self.tablero[x, y], self.tablero[x-1, y] = self.tablero[x-1, y], self.tablero[x, y]
            return True
        return False
    def mover_izquierda(self):
        x, y = self.poscicion_cero()
        if y-1 >= 0:
            self.tablero[x, y], self.tablero[x, y-1] = self.tablero[x, y-1], self.tablero[x, y]
            return True
        return False
    def mover_abajo(self):
        x, y = self.poscicion_cero()
        if x+1 <= 2:
            self.tablero[x, y], self.tablero[x+1, y] = self.tablero[x+1, y], self.tablero[x, y]
            return True
        return False
    def mover_derecha(self):
        x, y = self.poscicion_cero()
        if y+1 <= 2:
            self.tablero[x, y], self.tablero[x, y+1] = self.tablero[x, y+1], self.tablero[x, y]
            return True
        return False
    
    def imprimir_nodo(self):
        print(f'{self.tablero} - gn:{self.gn} - hn:{self.hn} - fn:{self.fn}\n accion: {self.accion} \n')
    
