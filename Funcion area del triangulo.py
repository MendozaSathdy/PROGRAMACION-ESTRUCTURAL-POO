def calcula_area_triangulo(base, altura):
    return (base * altura) / 2


base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

area = calcula_area_triangulo(base, altura)

print(f"El área del triángulo es: {area}")