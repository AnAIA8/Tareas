import math

def calcular_mcd(a, b):
    return math.gcd(a, b)

def calcular_mcm(a, b):
    if a == 0:
        return 0
    return abs(a * b) // calcular_mcd(a, b)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

mcd = calcular_mcd(numero1, numero2)
mcm = calcular_mcm(numero1 ,numero2)

print(f"El MCD de {numero1} y {numero2} es: {mcd}")
print(f"El MCM de {numero1} y {numero2} es: {mcm}")
