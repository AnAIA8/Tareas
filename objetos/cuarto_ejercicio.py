import os

os.system("clear")
class Calculadora():
    def __init__(self, p_numero, s_numero):
        self.p_numero = p_numero
        self.s_numero = s_numero
    def suma(self):
        return self.p_numero + self.s_numero

    def resta(self):
        return self.p_numero - self.s_numero

    def multi(self):
        return self.p_numero * self.s_numero

    def div(self):
        return self.p_numero / self.s_numero
    
    def __str__(self):
        return f"El resultado de la suma es: {self.suma()}\nEl resultado de la resta es: {self.resta()}\nEl resultado de la multiplicación es: {self.multi()}\nEl resulatdo de la división es: {round(self.div())}"


while True:
    p_numero = int(input("Ingrese el primer número: "))
    s_numero = int(input("Ingrese el segundo número: "))
    os.system("clear")
    print(Calculadora(p_numero, s_numero))
    print("Ingrese ENTER para continuar")
    input()
    os.system("clear")
