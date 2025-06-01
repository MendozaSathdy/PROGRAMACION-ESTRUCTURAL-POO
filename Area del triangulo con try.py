class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Calcular:
    def obtener_datos(self):
        while True:
            try:
                print("Ingresa la base del triángulo")
                base = float(input())
                print("Ingresa la altura del triángulo")
                altura = float(input())
                return Triangulo(base, altura)
            except ValueError:
                print("ingresa números válidos")

    def imprimir_resultado(self, area):
        print("El área del triángulo es: ", area)

def main():
    calcular = Calcular()
    triangulo = calcular.obtener_datos()
    area = triangulo.calcular_area()
    calcular.imprimir_resultado(area)

if __name__ == '__main__':
    main()