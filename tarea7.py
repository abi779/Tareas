class Clase:
    def __init__(self, atributo):
        #init va con dos guiones bajos al inicio y al final
        self.atributo = atributo

    def metodo(self):
        return "El atributo es: " + self.atributo
    
    def imprimir(self):
        print("Imprimiendo: " + self.atributo )

instancia = Clase("valor")
print(instancia.metodo() )
instancia.imprimir()
#ejercicio: crear una clase que sume dos numeros y los muestre por pantalla
class Suma:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular_suma(self):
        return self.numero1 + self.numero2

    def mostrar_resultado(self):
        print("La suma es: " + str(self.calcular_s
