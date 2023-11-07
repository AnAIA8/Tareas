def calcular_cuadrados(muestra):
    cuadrados = [x ** 2 for x in muestra]
    return cuadrados

numeros = int(input("Ingrese un número: ")), int(input("Ingrese otro número: ")), int(input("Ingrese otro número: ")), int(input("Ingrese otro número: ")), int(input("Ingrese otro número: "))
cuadrados = calcular_cuadrados(numeros)
print(f"Los cuadrados de la muestra de números son: {cuadrados}")