from tkinter.tix import Tk
from Ventana import Ventana

def main():

    jugador = "p1"
    root = Tk()
    root.wm_title("Conecta 4")
    app = Ventana(root, jugador)
    app.mainloop()
        
if __name__=="__main__":
    main()

