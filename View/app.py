import tkinter as tk
from Model.modelo import Compuertas
from View.pop import PopUp
from Controller.Tabla import Imagen

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("COMPUERTAS LOGICAS")
        self.geometry("800x400")
        self.config(bg="#000")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.add_widgets()
        self.compuerta=Compuertas()


    def  add_widgets(self):

        frame1 = tk.Frame(self, width=700, height=200, bd=5, relief="solid", bg="white")
        frame1.grid(row=0, column=0, padx=20, pady=(20, 10)) 

        lbl = tk.Label(frame1, text="Ingrese La compuerta logica:", bg="#000", fg="#fff", font=("Arial", 15))
        lbl.grid(sticky='w', padx=5, pady=5)

        self.entry = tk.Entry(frame1, width=50, font=("Arial", 12))
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        frame2 = tk.Frame(self, bd=5, relief="solid", bg="white")
        frame2.grid(row=1, column=0, padx=20, pady=(20, 10)) 

        boton = tk.Button(frame2, text="Enviar", width=10, height=2, bg="#2ecc71", fg="#fff", border="5", cursor="hand2", command=self.getData)
        boton.grid(row=1, column=0, sticky="nsew")

        botonClean = tk.Button(frame2, text="Borrar", width=10, height=2, bg="red", fg="#fff", border="5", cursor="hand2")
        botonClean.grid(row=1, column=1, sticky="nsew")

        frame3=tk.Frame(self, width=700, height=200, relief="solid", bg="white")
        frame3.grid(row=2, column=0, padx=60, pady=60)

        lbl2=tk.Label(frame3, text="MOSTRAR FIGURA", bg="#000", fg="#fff", font=("Arial", 20))
        lbl2.grid(row=0, column=0, sticky="nsew")

        botonShow=tk.Button(frame3,text="Mostrar", bg="#2ecc71", fg="#fff", width=10, height=2, border="5", cursor="hand2", command=self.tabla)
        botonShow.grid(row=1, column=0, sticky="nsew")

    def getData(self):
        try:
            valor = str(self.entry.get()).lower()

            if valor:
                self.compuerta.setNombre(valor)
                getValue=self.compuerta.getNombre()
                self.pop=PopUp()
                self.pop.show(getValue)
            else:
                pass
        except ValueError:
            self.entry.config(text="Error: Ingresa un valor numérico válido")

    def tabla(self):
    
        try:
            valor = str(self.entry.get()).lower()
            if valor:
                self.imagen = Imagen()
                self.imagen.addImage(valor)
            else:
                print("Error: El valor está vacío")
        except Exception as e:
            print("Error:", e)
    

        

