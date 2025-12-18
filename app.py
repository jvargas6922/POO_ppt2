"""
metodos de clases
@classmethod
Definicion:
    Es un metodo que pertenece a la clase en lugar de a una instancia de la clase.
    El primer parametro es la clase misma, convencionalmente llamado 'cls'.
    Definicion 'cls': Es una referencia a la clase, similar a 'self' que es una referencia a la instancia.

Ejemplo:
class Persona:
    poblacion = 0  # atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre  # atributo de instancia
        Persona.poblacion += 1

    @classmethod
    def mostrar_poblacion(cls):
        return f"Población actual: {cls.poblacion}"


metodos estaticos
@staticmethod
Definicion:
    Es un metodo que no recibe automaticamente una referencia a la instancia o a la clase.
    No puede acceder ni modificar el estado de la instancia o de la clase.

Ejemplo:
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b
            print("El precio no puede ser negativo.")
        
"""

"""
Uso de @classmethod 
"""
# ejemplo de uso de @classmethod

class Animal:
    # atributo de clase
    especie = "Canino"  

    # constructor
    def __init__(self, nombre):
        self.nombre = nombre  # atributo de instancia

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie


#crear instancia.
# animal  = Animal("Firulais")
# print(f"Nombre: {animal.nombre}, Especie: {animal.especie}")
# print("-----------------------------------")
# #cambiar especie usando metodo de clase
# Animal.cambiar_especie("Felino")
# print(f"Nombre: {animal.nombre}, Especie: {animal.especie}")
# print("-----------------------------------")
# Animal.cambiar_especie("Ave")
# print(f"Nombre: {animal.nombre}, Especie: {animal.especie}")


"""
Uso de @staticmethod
"""
# ejemplo de uso de @staticmethod

class Calculadora:
    # metodo estatico
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero."
        
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def restar(a, b):
        return a - b
        
# uso del metodo estatico sin crear instancia
resultado_1 = Calculadora.sumar(10, 5)
resultado_2 = Calculadora.restar(10, 5)
resultado_3 = Calculadora.multiplicar(10, 5)
resultado_4 = Calculadora.dividir(10, 0)
print(f"Suma: {resultado_1}")
print(f"Resta: {resultado_2}")
print(f"Multiplicación: {resultado_3}")
print(f"División: {resultado_4}")
