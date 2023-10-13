import os

os.system("clear")
class Alumno():
    def __init__(self, nombre=None):
        self.nombre = nombre
        self.nota = 0

alumnos = []

cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cant_alumnos):
    alumno = Alumno()
    alumno.nombre = input("Ingrese el nombre del alumno "+str(i+1)+" :")
    alumnos.append(alumno)

os.system("clear")
while True:
    print("Seleccione un alumno de la lista:")
    CONTADOR = 1
    for alumno in alumnos:
        print(str(CONTADOR)+". "+str(alumno.nombre))
        CONTADOR += 1
    nro_alumno = int(input())
    os.system("clear")
    nota = int(input("Ingrese la nota del alumno: "))
    if nota <= 1:
        alumno = alumnos[nro_alumno-1]
        print("La nota del alumno "+str(alumno.nombre)+" es ", nota, "y ha reprobado ")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    else:
        alumno = alumnos[nro_alumno-1]
        print("La nota del alumno "+str(alumno.nombre)+" es", nota, " ha aprobado ")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
