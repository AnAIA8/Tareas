import os

os.system("clear")
class Persona():
    def __init__(self, nombre=None):
        self.nombre = nombre
        self.edad = 0

personas = []

cant_personas = int(input("Ingrese la cantidad de personas: "))

for i in range(cant_personas):
    persona = Persona()
    persona.nombre = input("Ingrese el nombre de la persona: ")
    personas.append(persona)

os.system("clear")

while True:
    print("Seleccione una persona de la lista: ")
    CONTADOR = 1
    for persona in personas:
        print(str(CONTADOR)+"."+str(persona.nombre))
        CONTADOR += 1
    nro_persona = int(input())
    os.system("clear")
    edad = int(input("Ingrese la edad de la persona: "))
    if edad < 18:
        persona = personas[nro_persona-1]
        print("La persona se llama "+str(persona.nombre)+" tiene ", edad, "años"+" y es menor de edad")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    else:
        persona = personas[nro_persona-1]
        print("La persona se llama "+str(persona.nombre)+" tiene ", edad, "años"+" y es mayor de edad")
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
