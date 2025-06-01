class Sumador:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.suma = 0

    def obtener_valores(self):
        self.num1 = int(input("Ingresa el num1: "))
        self.num2 = int(input("Ingresa el num2: "))  

    def calcular_suma(self):
        self.suma = self.num1 + self.num2

    def mostrar_resultado(self):
        print(f"El valor de la suma es {self.suma}")

def main():
    sumador = Sumador()
    sumador.obtener_valores()
    sumador.calcular_suma()
    sumador.mostrar_resultado()

if __name__ == "__main__":
    main()