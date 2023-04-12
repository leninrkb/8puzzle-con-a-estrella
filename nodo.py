import numpy as np
class Nodo:
    def __init__(self):
        self.tablero = np.array([
            [7, 1, 8],
            [6, 3, 0],
            [2, 5, 4],
        ])
        self.padre = None
        self.gn = 0
        self.hn = 0
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