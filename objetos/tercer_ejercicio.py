import os

os.system("clear")
class Triangulo():
    def __init__(self, nombre=None):
        self.nombre = nombre
        self.p_lado = 0
        self.s_lado = 0
        self.t_lado = 0

triangulos = []

cant_triangulos = int(input("Ingrese la cantidad "))

for i in range(cant_triangulos):
    triangulo = Triangulo()
    triangulo.nombre = input("Ingrese un triángulo: ")
    triangulos.append(triangulo)

os.system("clear")
while True:
    print("Seleccione un triángulo de la lista:")
    CONTADOR = 1
    for triangulo in triangulos:
        print(str(CONTADOR)+"."+str(triangulo.nombre))
        CONTADOR += 1
    nro_triangulo = int(input())
    os.system("clear")
    p_lado = int(input("Ingrese el valor del primer lado: "))
    s_lado = int(input("Ingrese el valor del segundo lado: "))
    t_lado = int(input("Ingrese el valor del tercer lado: "))
    if p_lado == s_lado and s_lado == t_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" tiene los tres lados iguales y es equilátero")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif p_lado == s_lado and p_lado > t_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es isósceles")
        print("El primer y segundo lado son iguales y son los mayores")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif p_lado == s_lado and p_lado < t_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es isósceles")
        print("El tercer lado es el mayor")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif p_lado == t_lado and p_lado > s_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es isósceles")
        print("El primer y tercer lado son iguales y son los mayores")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif p_lado == t_lado and p_lado < s_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es isósceles")
        print("El segundo lado es el mayor")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif s_lado == t_lado and s_lado > p_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es isósceles")
        print("El segundo y el tercer lado  son iguales y son los mayores")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif s_lado == t_lado and s_lado < p_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es isósceles")
        print("El primer lado es el mayor")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif s_lado > t_lado > p_lado or s_lado > p_lado > t_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es escaleno")
        print("El lado mayor es el segundo")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif t_lado > s_lado > p_lado or t_lado > p_lado > s_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es escaleno")
        print("El lado mayor es el tercero")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif p_lado > s_lado > t_lado or p_lado > t_lado > s_lado:
        triangulo = triangulos[nro_triangulo-1]
        print("El triángulo "+str(triangulo.nombre)+" es escaleno")
        print("El lado mayor es el primero")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
