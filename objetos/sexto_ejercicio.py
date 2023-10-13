import os

os.system("clear")
class Animal():
    def __init__(self, cant_extre=None, familia=None, peso=None):
        self.cant_extre = cant_extre
        self.peso = peso
        self.familia = familia

class Perro(Animal):
    def __init__(self, cant_extre,familia, edad=None, peso=None):
        super().__init__(cant_extre, familia, peso)
        self.edad = edad
    def __str__(self):
        return f"Extremidades: {self.cant_extre}\nPeso: {self.peso}\nFamilia:{self.familia}\nEdad: {self.edad}"
while True:
    CANT_EXTRE = int(4)
    FAMILIA = str("Canino")
    peso = int(input("Ingrese el peso: "))
    edad = int(input("Ingrese la edad: "))
    os.system("clear")
    print(Perro(CANT_EXTRE, FAMILIA, peso, edad))
    print("Presione ENTER para continuar")
    input()
    os.system("clear")
    