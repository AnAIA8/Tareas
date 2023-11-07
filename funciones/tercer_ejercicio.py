import math 

def calcular_factorial(numero):
    if numero < 0:
        return None
    return math.factorial(numero)

numero = int(input("Ingrese un número: "))
resultado = calcular_factorial(numero)
print(resultado)