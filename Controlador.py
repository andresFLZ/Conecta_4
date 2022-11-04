from Tablero import Tablero

class Controlador:

    def __init__(self):
        self.fichas_p1 = 21
        self.fichas_p2 = 21
        self.tablero = Tablero()

    def validar_columna_disponible(self, columna):

        def validar_posicion_disponible(columna):
            for i in range(6):
                if self.tablero.devolver_valor(i, columna) == 0:
                    return True
            return False

        while True:
            try:
                posicion = int(columna)
                if posicion < 1 or posicion > 7:
                    return 1
                elif validar_posicion_disponible(posicion - 1) == False:
                    return 2
                break
            except ValueError:
                return 3
        return 4

    def jugar(self, jugador, columna):

        def fila_disponible(columna):
            for i in range(5, -1, -1):
                if self.tablero.devolver_valor(i, columna) == 0:
                    return i
        
        def ubicar_ficha(posicion, jugador):
            if jugador == "p1":
                self.tablero.cambiar_valor(posicion[0], posicion[1], 1)
                self.fichas_p1 -= 1
            else:
                self.tablero.cambiar_valor(posicion[0], posicion[1], 2)
                self.fichas_p2 -= 1

        fila = fila_disponible(columna)
        posicion = [fila, columna]

        ubicar_ficha(posicion, jugador)

    def devolver_tablero(self):
        return self.tablero

    def devolver_valor(self, fila, columna):
        return self.tablero.devolver_valor(fila, columna)

    def juego_terminado(self, jugador):

        def es_ganador(jugador):

            def en_linea_4(valor, lista):
                contador = 0

                for i in range(len(lista)):
                    if lista[i] == valor:
                        contador += 1
                        if contador == 4:
                            break
                    else:
                        contador = 0

                return contador == 4

            def ganador_vertical(valor):
                nums_columna = []
                for columna in range(7):
                    for fila in range(6):
                        nums_columna.append(self.tablero.devolver_valor(fila, columna))
                    if en_linea_4(valor, nums_columna) == True:
                        return True
                    nums_columna = []
                return False

            def ganador_horizontal(valor):
                nums_fila = []
                for fila in range(6):
                    for columna in range(7):
                        nums_fila.append(self.tablero.devolver_valor(fila, columna))
                    if en_linea_4(valor, nums_fila) == True:
                        return True
                    nums_fila = []
                return False

            def ganador_diagonal(valor):

                def diagonal_normal(valor):

                    nums_diagonal = []
                    fila = 5
                    columna = 0
                    for i in range(6):
                        while fila < 6:
                            nums_diagonal.append(self.tablero.devolver_valor(fila, columna))
                            fila += 1
                            columna += 1
                        if en_linea_4(valor, nums_diagonal):
                            return True
                        nums_diagonal = []
                        fila -= (i+2)
                        columna = 0

                    for i in range(6):
                        nums_diagonal = []
                        columna = i+1
                        fila = 0
                        while columna < 7:
                            nums_diagonal.append(self.tablero.devolver_valor(fila, columna))
                            fila += 1
                            columna += 1
                        if en_linea_4(valor, nums_diagonal):
                            return True

                    return False

                def diagonal_inversa(valor):

                    for i in range(12):
                        nums_diagonal = []
                        for fila in range(6):
                            for columna in range(7):
                                if fila + columna == i:
                                    nums_diagonal.append(self.tablero.devolver_valor(fila, columna))
                        if en_linea_4(valor, nums_diagonal):
                            return True        
                        
                    return False

                if diagonal_normal(valor) or diagonal_inversa(valor):
                    return True
                else:
                    return False

            if jugador == "p1":
                valor = 1
            else:
                valor = 2

            if ganador_vertical(valor) == True or ganador_horizontal(valor) == True or ganador_diagonal(valor) == True:
                return True
            else:
                return False

        if self.fichas_p1 == 0 and self.fichas_p2 == 0:
            return True
        elif es_ganador(jugador):
            return True
        else:
            return False

    def reiniciar_tablero(self):
        self.fichas_p1 = 21
        self.fichas_p2 = 21
        self.tablero = Tablero()