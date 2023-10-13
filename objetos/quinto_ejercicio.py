import os

os.system("clear")
class Agenda():
    def __init__(self, nombre=None, email=None):
        self.nombre = nombre
        self.telefono = 0
        self. email = email
        self.contactos = []

    def añadir(self, nombre, telefono, email):
        contacto = Agenda(nombre, email)
        self.contactos.append(contacto)

    def lista(self):
        for contacto in self.contactos:
            print(contacto.nombre)

    def buscar(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("Nombre:", contacto.nombre)
                print("Teléfono:", contacto.telefono)
                print("Email:", contacto.email)
                return
        print("Contacto no encontrado.")

    def editar(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                n_nombre = input("Ingrese el nuevo nombre: ")
                n_telefono = int(input("Ingrese el nuevo teléfono:"))
                n_email = input("Ingrese el nuevo email:")
                contacto.nombre = n_nombre
                contacto.telefono = n_telefono
                contacto.email = n_email
                print("Contacto actualizado.")
                return
            print("Contacto no encontrado.")

agenda = Agenda()

while True:
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")

    opcion = input("Ingrese la opción deseada: ")
    os.system("clear")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("Ingrese el telefono:"))
        email = input("Ingrese el email: ")
        agenda.añadir(nombre, telefono, email)
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif opcion == "2":
        agenda.lista()
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        agenda.buscar(nombre)
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a editar: ")
        agenda.editar(nombre)
        print("Presione ENTER para continuar")
        input()
        os.system("clear")
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
        os.system("clear")
