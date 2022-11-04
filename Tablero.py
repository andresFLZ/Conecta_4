class Tablero:
    
    def __init__(self):
        self.tablero = self.crear_matriz()
    
    def crear_matriz(self):
        matriz = []
        for i in range(6):
            matriz.append([])
            for j in range(7):
                matriz[i].append(0)
        return matriz

    def devolver_valor(self, fila, columna):
        return self.tablero[fila][columna]

    def cambiar_valor(self, fila, columna, valor):
        self.tablero[fila][columna] = valor