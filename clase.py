"""
Clase POO en python (PPT2)

atributos de la clases pueden ser:
- publicos => self.nombre_atributo 
- privados => self.__nombre_atributo
- protegidos => self._nombre_atributo

Diferencias entre los atributos:
Publicos:
    - Accesibles desde cualquier parte del codigo.
    - pueden ser modificados desde fuera de la clase.
    - Ejemplo: self.nombre

Privados:
    - Accesibles solo desde dentro de la clase.
    - No pueden ser accedidos ni modificados desde fuera de la clase.
    - Ejemplo: self.__nombre

Protegidos:
    - Accesibles desde la clase y sus subclases.
    - No pueden ser accedidos desde fuera de la clase, pero si desde sus subclases.
    - Ejemplo: self._nombre


"""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre # atributo publico
        self.__edad = 30 # atributo privado
        self._altura = 1.75 # atributo protegido

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

"""
Vamos a modelar un libro como objeto con tres atributos y un método para mostrar sus datos.(listo)
1. Definir la clase Libro con los atributos titulo, autor, anio (listo)
2. Agregar un método mostrar_info() que imprima todos los datos (listo)
3. Crear dos objetos Libro diferentes (listo)
4. Llamar al método mostrar_info() de cada objeto (listo)
📌 Objetivo: reforzar cómo se usan múltiples atributos, cómo funcionan los métodos, y
cómo crear varios objetos con datos distintos.
"""

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")

    def autor(self):
        return f"{self.autor}"
        # return self.autor

    def anio(self):
        return self.anio # int
        # print(type(self.anio))
        # return f"{self.anio}" # str


"""
¿En qué consistirá la Demo?
Vamos a crear una clase que representa una cuenta de correo electrónico, con atributos públicos, protegidos y
privados para simular distintos niveles de acceso.
1. Definir la clase CuentaCorreo (listo)
2. Crear una instancia
3. Acceder a los atributos
4. Reflexión final:
a. ¿Qué pasaría si esta clase se usara en un sistema real sin protección?
📌 Objetivo: reforzar la utilidad del encapsulamiento en contextos sensibles, mostrando
cómo Python permite proteger atributos para evitar mal uso o manipulación directa.
"""

class CuentaCorreo:
    def __init__(self, email, password, servidor):
        self.email = email  # atributo publico
        self.__password = password  # atributo privado
        self._servidor = servidor  # atributo protegido

    def mostrar_info(self):
        print(f"Email: {self.email}")
        print(f"Servidor: {self._servidor}")
        # No mostramos la contraseña por seguridad

    # Acceder al atributo privado de la siguiente forma:
    # Getter  me permiten acceder a atributos privados
    def get_password(self):
        return self.__password # valor self.__password
    
    # Setter me permiten modificar atributos privados
    def set_password(self, nuevo_password):
        self.__password = nuevo_password

class Cuenta:
    def __init__(self):
        self.__saldo = 0  # atributo privado

    # getter
    def get_saldo(self):
        return self.__saldo
    
    # setter
    def set_saldo(self, monto):
        if monto >= 0:
            self.__saldo = monto
        else:
            print("El saldo no puede ser negativo.")

    def validar_monto(self, monto):
        if  monto.isdigit():
            return True
        else:
            return False
        
"""
Vas a diseñar una clase que represente un producto de tienda, controlando el acceso y modificación del precio a
través de métodos específicos.
1.🔹 Qué debe tener la clase:
    ● Un atributo público para el nombre del producto (listo)
    ● Un atributo privado para el precio (__precio) (listo)
    ● Un método para ver el precio (getter) (listo)
    ● Un método para modificar el precio (setter), que solo permita valores positivos (listo)
    ● En el constructor (__init__), usar el setter para validar el precio desde el inicio (listo)
2.🔹 Qué se debe probar con objetos:
    ● Crear un producto con precio válido
    ● Mostrar el precio usando el getter
    ● Intentar cambiar el precio a un valor negativo (debe mostrar un error)
    ● Modificar correctamente el precio y verificar el nuevo valor
"""
class Producto:
    def __init__(self,nombre, precio):
        self.nombre = nombre  # atributo publico
        self.set_precio(precio)  # usar el setter para validar el precio

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")

"""
¿En qué consistirá la Demo?
Vas a diseñar una clase que modele un empleado, incorporando tanto un método de clase como uno estático
para aplicar distintos tipos de comportamiento.
1.🔹 Lo que deberá tener la clase:
    ● Atributos públicos como nombre y salario (listo)
    ● Un atributo de clase llamado aumento_general con un valor inicial (ej. 1.05) (listo)
    ● Un método de clase que permita modificar el porcentaje de aumento general para todos los empleados (listo)
    ● Un método estático que reciba un salario y verifique si supera un cierto umbral (ej.sueldo mínimo)(listo)
2.🔹 Qué se debe probar:
    ● Crear varios empleados con salarios distintos
    ● Modificar el aumento general desde la clase
    ● Usar el método estático para evaluar si un salario es alto 
"""

class Empleado:
    # atributos publicos
    aumento_general = 1.05

    # constructor
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    @classmethod
    def modificar_aumento_general(cls, nuevo_aumento):
        cls.aumento_general = nuevo_aumento

    @staticmethod
    def es_sueldo_alto(salario, umbral=500000): # unbral = 3000 es un valor por defecto
        return salario > umbral # una condicion que devuelve True o False
    
# Primera instancia de la clase.
# empleado_1 = Empleado("Ana", 600000)
# print(f"Nombre empleado: {empleado_1.nombre}, Salario: {empleado_1.salario}")
# aumento_1 = Empleado.aumento_general
# print(f"Aumento general actual: {aumento_1}")
# print(f"El aumento del empleado {empleado_1.nombre} es: {empleado_1.salario * aumento_1}")
# # verificacion si el sueldo es alto de este trabajador
# if Empleado.es_sueldo_alto(empleado_1.salario):
#     print(f"El salario de {empleado_1.nombre} es alto.")
# else:
#     print(f"El salario de {empleado_1.nombre} es bajo.")

# print("-----------------------------------")

# empleado_2 = Empleado("Luis", 400000)
# print(f"Nombre empleado: {empleado_2.nombre}, Salario: {empleado_2.salario}")
# Empleado.modificar_aumento_general(1.20)
# aumento_2 = Empleado.aumento_general
# print(f"Aumento general actual: {aumento_2}")
# print(f"El aumento del empleado {empleado_2.nombre} es: {empleado_2.salario * aumento_2}")
# if Empleado.es_sueldo_alto(empleado_2.salario, umbral=600000):
#     print(f"El salario de {empleado_2.nombre} es alto.")
# else:
#     print(f"El salario de {empleado_2.nombre} es bajo.")

# print("-----------------------------------")
# empleado_3 = Empleado("Jorge", 700000)
# print(f"Nombre empleado: {empleado_3.nombre}, Salario: {empleado_3.salario}")
# Empleado.modificar_aumento_general(3.00)
# aumento_3 = Empleado.aumento_general
# print(f"Aumento general actual: {Empleado.aumento_general}")
# print(f"valor del salio: {empleado_3.salario}")
# print(f"valor del aumento: {aumento_3}")
# print(f"El aumento del empleado {empleado_3.nombre} es: {empleado_3.salario * aumento_3}")
# if Empleado.es_sueldo_alto(empleado_3.salario, umbral=700000):
#     print(f"El salario de {empleado_3.nombre} es alto.")
# else:
#     print(f"El salario de {empleado_3.nombre} es bajo.")



    
