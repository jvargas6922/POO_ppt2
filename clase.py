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

    
    