import tkinter as tk

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Calcular:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de Área de Triángulo")
        self.crear_widgets()
        self.ventana.geometry("300x300")

    def crear_widgets(self):
        self.etiqueta_base = tk.Label(self.ventana, text="Ingresa la base del triángulo")
        self.etiqueta_base.pack()
        self.entry_base = tk.Entry(self.ventana)
        self.entry_base.pack()

        self.etiqueta_altura = tk.Label(self.ventana, text="Ingresa la altura del triángulo")
        self.etiqueta_altura.pack()
        self.entry_altura = tk.Entry(self.ventana)
        self.entry_altura.pack()

        self.boton_calcular = tk.Button(self.ventana, text="Calcular Área", command=self.calcular_area)
        self.boton_calcular.pack()

        self.etiqueta_resultado = tk.Label(self.ventana, text="Resultado")
        self.etiqueta_resultado.pack()
        self.label_resultado = tk.Label(self.ventana, text="")
        self.label_resultado.pack()

    def calcular_area(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            triangulo = Triangulo(base, altura)
            area = triangulo.calcular_area()
            self.label_resultado.config(text=f"El área del triángulo es: {area}")
        except ValueError:
            self.label_resultado.config(text="Ingresa números válidos")

    def run(self):
        self.ventana.mainloop()

def main():
    calcular = Calcular()
    calcular.run()

if __name__ == '__main__':
    main()