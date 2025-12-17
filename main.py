# importar el archivo donde tengo la clase creada
from clase import Persona,Libro, CuentaCorreo

# instancia de la clase Persona
# persona = Persona("Joffred")
# persona.saludar()

# Accediendo al atributo publico
# print("Nombre (publico):", persona.nombre)

# Accediendo al atributo privado (esto generará un error)
#print("Edad (privado):", persona.__edad)  # AttributeError

# Accediendo al atributo protegido (no recomendado, pero posible)
# print("Altura (protegido):", persona._altura)  # 1.

# libros_nuevos = 2000

# libro_1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
# libro_1.mostrar_info()

# if libro_1.anio > libros_nuevos:
#     print("El libro es relativamente nuevo.")
# else:
#     print("El libro es antiguo.")

# print("**********" * 10)

# libro_2 = Libro("La casa de los espiritus","Isabel Allende",1982)
# libro_2.mostrar_info()
# if libro_2.anio > libros_nuevos:
#     print("El libro es relativamente nuevo.")
# else:
#     print("El libro es antiguo.")

email = input("Ingrese su correo electrónico: ")
contrasena = input("Ingrese su contraseña: ")
servidor = input("Ingrese el servidor de correo (e.g., smtp.example.com): ")

# instancia de la clase CuentaCorreo
cuenta_correo = CuentaCorreo(email, contrasena, servidor)
# metodo para mostrar la info del correo
cuenta_correo.mostrar_info()

# para acceder al atributo privado (password)
password = cuenta_correo.get_password()
print("Contraseña:", password)

password_nuevo = input("Ingrese la nueva contraseña: ")
# para modificar el atributo privado (password)
cuenta_correo.set_password(password_nuevo)

# para acceder al atributo privado (password)
password = cuenta_correo.get_password()
print("Nueva contraseña:", password)