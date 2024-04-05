from prettytable import PrettyTable
import tkinter as tk
from Controller.controlador import Controller


class PopUp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Compuertas")
        self.geometry("600x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.control=Controller()
        self.addWigets()

    def addWigets(self):
        self.lblTittle=tk.Label(self, text="", fg='#2ecc71' , font=("Arial", 20),)
        self.lblTittle.grid( column=0 , row=0)

        frame1 = tk.Frame(self, width=600, height=500, bd=5, relief="solid", bg="white" )
        frame1.grid(row=1, column=0, padx=20, pady=(20, 10)) 

        self.output_label = tk.Label(frame1, text="", bg="white", width=20, font=("Arial", 25), fg= "black")
        self.output_label.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

        frame2 = tk.Frame(self, bd=5, relief="solid", bg="red")
        frame2.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="nsew") 

        self.outAxioma = tk.Label(frame2, text="", bg="red", font=("Arial", 25), fg="#2ecc71", wraplength=580)
        self.outAxioma.pack(expand=True, fill="both", padx=10, pady=10, anchor="center")

    
    def show(self, value):
        self.lblTittle["text"] = "COMPUERTA",value.upper()
        compuerta = self.control.get_compuerta(value)
        if compuerta is not None:
           textoAxioma = f"Axioma: {compuerta.axioma}\n"
           texto = "Tabla de verdad \n{}\n".format(compuerta.tabla.get_string())
           self.output_label["text"] = texto
           self.outAxioma["text"]= textoAxioma
           return compuerta.simbolo
        else:
           self.output_label["text"] = "Compuerta no encontrada"
           return None


  





    

        