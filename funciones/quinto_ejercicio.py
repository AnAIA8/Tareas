import math

def calcular_area_circulo(radio):
    return math.pi * radio **2

def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen

radio_circulo = float(input("Ingrse el radio del círculo: "))
area = calcular_area_circulo(radio_circulo)
print(f"Área del círculo con radio {radio_circulo}: {area}")

radio_cilindro = float(input("Ingrese el radio del cilindro: "))
altura_cilindro = float(input("Ingrese la altura del cilindro: "))
volumen = calcular_volumen_cilindro(radio_cilindro, altura_cilindro)
print(f"Volumen del cilindro con radio {radio_cilindro} y altura {altura_cilindro}: {volumen}")