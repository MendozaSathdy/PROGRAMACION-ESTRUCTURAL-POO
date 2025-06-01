import tkinter as tk

class OperacionSuma:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Operación de Suma")
        self.ventana.geometry("500x500")

        
        self.interfaz()

        self.ventana.mainloop()

    def interfaz(self):
        
        tk.Label(self.ventana, text="Ingresa tu primer num:").pack()
        self.entrada_prim = tk.Entry(self.ventana)
        self.entrada_prim.pack()

        
        tk.Label(self.ventana, text="Ingresa tu segundo num:").pack()
        self.entrada_seg = tk.Entry(self.ventana)
        self.entrada_seg.pack()

      
        tk.Button(self.ventana, text="Suma", command=self.suma).pack()

        self.etiqueta_resultado = tk.Label(self.ventana, text="")
        self.etiqueta_resultado.pack()

    def suma(self):
        try:
            num1 = int(self.entrada_prim.get())
            num2 = int(self.entrada_seg.get())
            resultado = num2 + num2
            self.etiqueta_resultado.config(text=f"Su 1er num es {num1}, su 2do num es {num2}, y su resultado de la suma es {resultado}")
        except ValueError:
            self.etiqueta_resultado.config(text="Error: Ingresa numeros.")

def main():
    OperacionSuma()

if __name__ == "__main__":
    main()