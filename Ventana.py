from tkinter import Frame, Tk, Label, Button, Entry, messagebox
from Controlador import Controlador

class Ventana(Frame):

    def __init__(self, master=None, jugador="p1"):
        super().__init__(master, width=500, height=600, bg="#C9F88C")
        self.master = master
        self.columna = ""
        self.victorias_p1 = 0
        self.victorias_p2 = 0
        self.jugador = jugador
        self.pack()
        self.controlador = Controlador()
        self.crear_objetos()

    def crear_objetos(self):

        def crear_tablero():
            for i in range(7):
                Label(self.f_tablero, text=str(i+1),foreground="red").grid(row=0, column=i, padx=5, pady=5)

            self.imprimir_tablero()

        self.f_tablero = Frame(self,width=425, height=400, bg="#8FF566")
        self.f_tablero.pack(side='top', padx=10, pady=10)

        f_controlador = Frame(self,width=425, height=100, bg="#8FF566")
        f_controlador.pack(side='bottom', padx=10, pady=10)

        f_v_p1 = Frame(f_controlador, width=90, height=80)
        f_v_p1.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
        l_tv_p1 = Label(f_v_p1, text="Victorias p1")
        l_tv_p1.pack(side="left", padx=5, pady=5)
        self.l_nv_p1 = Label(f_v_p1, text=str(self.victorias_p1))
        self.l_nv_p1.pack(side="right", padx=5, pady=5)

        f_v_p2 = Frame(f_controlador, width=90, height=80)
        f_v_p2.grid(row=0, column=3, rowspan=2, padx=5, pady=5)
        l_tv_p2 = Label(f_v_p2, text="Victorias p2")
        l_tv_p2.pack(side="right", padx=5, pady=5)
        self.l_nv_p2 = Label(f_v_p2, text=str(self.victorias_p1))
        self.l_nv_p2.pack(side="left", padx=5, pady=5)

        self.btn_reiniciar = Button(f_controlador, text="Reiniciar", command=self.btn_reiniciar)
        self.btn_reiniciar.grid(row=0, column=1, padx=5, pady=5)

        self.btn_resetear = Button(f_controlador, text="Resetear victorias", command=self.btn_resetear)
        self.btn_resetear.grid(row=0, column=2, padx=5, pady=5)

        f_jugador = Frame(f_controlador, width=90, height=80)
        f_jugador.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.l_turno = Label(f_jugador, text="Turno del jugador " + self.jugador)
        self.l_turno.grid(row=0, column=0, padx=5, pady=5)
        l_jugador = Label(f_jugador, text="¿En que columna deseas insertar la ficha?")
        l_jugador.grid(row=1, column=0, padx=5, pady=5)
        self.e_principal = Entry(f_jugador, width=2)
        self.e_principal.grid(row=2, column=0, padx=5, pady=5)
        self.btn_jugar = Button(f_jugador, text="JUGAR", command=self.btn_jugar)
        self.btn_jugar.grid(row=3, column=0, padx=5, pady=5)

        crear_tablero()

    def imprimir_tablero(self):

        for fila in range(6):
            for columna in range(7):

                if self.controlador.devolver_valor(fila, columna) == 0:
                    Label(self.f_tablero, background="white", width=1).grid(row=fila+1, column=columna, padx=5, pady=5)
                elif self.controlador.devolver_valor(fila, columna) == 1:
                    Label(self.f_tablero, background="red", width=1).grid(row=fila+1, column=columna, padx=5, pady=5)
                else:
                    Label(self.f_tablero, background="yellow", width=1).grid(row=fila+1, column=columna, padx=5, pady=5)

    def juego_terminado(self):
        return self.controlador.juego_terminado(self.jugador)

    def btn_jugar(self):
        
        def validar_columna():

            if self.controlador.validar_columna_disponible(self.columna) == 1:
                messagebox.showerror(title="Error", message="Oops!  No es un numero valido.")
                return False
            if self.controlador.validar_columna_disponible(self.columna) == 2:
                messagebox.showerror(title="Error", message="Oops!  La columna no tiene espacio.")
                return False
            if self.controlador.validar_columna_disponible(self.columna) == 3:
                messagebox.showerror(title="Error", message="Oops! Tienes que introducir un número.")
                return False
            return True

        def cambiar_jugador():
            if self.jugador == "p1":
                self.jugador = "p2"
            else:
                self.jugador = "p1"

            self.l_turno.config(text="Turno del jugador " + self.jugador)

        def modificar_victorias():

            if self.jugador == "p1":
                self.victorias_p1 += 1
                self.l_nv_p1.config(text=str(self.victorias_p1))
            else:
                self.victorias_p2 += 1
                self.l_nv_p2.config(text=str(self.victorias_p2))

        self.columna = self.e_principal.get() 

        if validar_columna() == False:
            self.e_principal.delete(0,'end')
            cambiar_jugador()
        else:
            self.e_principal.delete(0,'end')
            self.controlador.jugar(self.jugador, int(self.columna) -1)
            self.imprimir_tablero()

        if self.juego_terminado() == True:
            messagebox.showinfo(title="Ganador", message="el ganador es: " + self.jugador)
            modificar_victorias()
            self.reiniciar()
        else:
            cambiar_jugador()

    def btn_reiniciar(self):
        self.reiniciar()

    def btn_resetear(self):
        self.victorias_p2 = 0
        self.victorias_p1 = 0
        self.l_nv_p1.config(text=str(self.victorias_p1))
        self.l_nv_p2.config(text=str(self.victorias_p2))

    def reiniciar(self):
        self.controlador.reiniciar_tablero()
        self.imprimir_tablero()