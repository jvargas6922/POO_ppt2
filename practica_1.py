"""
Contexto: 🙌
Una librería necesita un sistema simple para controlar su inventario. Cada libro posee un título, un autor, un
precio y una cantidad de stock. Se desea evitar precios negativos y gestionar correctamente las ventas.
Consigna: ✍
    Modelá una clase Libro que contenga atributos,
    públicos y privados. Utilizá getters y setters para
    proteger el precio, y diseñá un método para realizar
    ventas que actualicen el stock.
Paso a paso: ⚙
0. Definir la clase Libro  (listo)
1. Definír los atributos: titulo, autor, stock (públicos) y __precio (privado) (listo)
2. Implementá get_precio() y set_precio() validando que sea un valor positivo (listo)
3. Agregá un método vender(unidades) que descuente del stock si hay suficiente (listo)
4. Creá el método mostrar_info() para imprimir todos los datos del libro (listo)
5. Probá con varios objetos (listo)
"""

class Libro:
    # atributo publico
    tipo_libro = "Fantasía"

    # constructor
    def __init__(self, titulo, autor, stock, precio):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
        self.__precio = precio  # atributo privado

    # getter
    def get_precio(self):
        return self.__precio
    
    # setter
    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("Error: El precio no puede ser negativo.")

    # Metodo de la clase
    @staticmethod
    def vender_unidades(self, unidades):
        if unidades <= self.stock:
            self.stock -= unidades
            print(f"Venta realizada: {unidades} unidades de '{self.titulo}' vendidas.")
        else:
            print(f"Error: No hay suficiente stock para vender {unidades} unidades de '{self.titulo}'.")


    @classmethod
    def cambiar_tipo_libro(cls, nuevo_tipo):
        cls.tipo_libro = nuevo_tipo

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Stock: {self.stock}")
        print(f"Precio: ${self.__precio}")
        print(f"Tipo de libro: {Libro.tipo_libro}")

# instancia de la clase Libro
print("Instancia 1")
libro_1 = Libro("Game of Thrones", "George R. R. Martin", 10, 50)
libro_1.mostrar_info()
print("----" * 10)
# Ver el precio del Libro
precio = libro_1.get_precio()
print(f"El precio del libro es: ${precio}")
print("----" * 10)
# modificar el precio del libro
libro_1.set_precio(60)
nuevo_precio = libro_1.get_precio()
print(f"El precio del libro es: ${nuevo_precio}")
Libro.vender_unidades(libro_1, 8)
libro_1.mostrar_info()

print("----" * 10)
print("Instancia 2")
libro_2 = Libro("Codigo Limpio", "Robert C. Martin", 5, 40)
Libro.cambiar_tipo_libro("Programación")
libro_2.mostrar_info()
# ver precio
libro_2.get_precio()
print("----" * 10)
# modificar el precio del libro
libro_2.set_precio(80)
nuevo_precio = libro_2.get_precio()
print(f"El precio del libro es: ${nuevo_precio}")
Libro.vender_unidades(libro_2, 6)

libro_2.mostrar_info()


