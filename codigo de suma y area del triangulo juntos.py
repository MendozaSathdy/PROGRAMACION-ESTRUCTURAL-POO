def area(texto_de_numa, texto_de_numb):
    numero_a = int(texto_de_numa)
    numero_b = int(texto_de_numb)
    area = (numero_a * numero_b) / 2
    return f"el area del triangulo es de : {area}"


def sumar(texto_de_numa, texto_de_numb):
    numero_a = int(texto_de_numa)
    numero_b = int(texto_de_numb)
    suma = numero_a + numero_b
    return f"La suma es: {suma}"


numa = input("ingrese la base: ")
numb = input("ingrese la altura: ")

resultado=area(numa, numb)
print(resultado)

resultado2=sumar(numa, numb)
print(resultado2)