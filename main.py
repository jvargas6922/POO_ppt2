# importar el archivo donde tengo la clase creada
from clase import Persona, Libro, CuentaCorreo, Cuenta, Producto, Empleado

"""
    Practica clase Persona
"""
# instancia de la clase Persona
# persona = Persona("Joffred")
# persona.saludar()

# Accediendo al atributo publico
# print("Nombre (publico):", persona.nombre)

# Accediendo al atributo privado (esto generará un error)
#print("Edad (privado):", persona.__edad)  # AttributeError

# Accediendo al atributo protegido (no recomendado, pero posible)
# print("Altura (protegido):", persona._altura)  # 1.

"""
    Practica clase Libro
"""
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


"""
    Practica clase CuentaCorreo
"""
# email = input("Ingrese su correo electrónico: ")
# contrasena = input("Ingrese su contraseña: ")
# servidor = input("Ingrese el servidor de correo (e.g., smtp.example.com): ")

# # instancia de la clase CuentaCorreo
# cuenta_correo = CuentaCorreo(email, contrasena, servidor)
# # metodo para mostrar la info del correo
# cuenta_correo.mostrar_info()

# # para acceder al atributo privado (password)
# password = cuenta_correo.get_password()
# print("Contraseña:", password)

# password_nuevo = input("Ingrese la nueva contraseña: ")
# # para modificar el atributo privado (password)
# cuenta_correo.set_password(password_nuevo)

# # para acceder al atributo privado (password)
# password = cuenta_correo.get_password()
# print("Nueva contraseña:", password)


# cuenta_corriente = Cuenta() # instancia de la clase Cuenta
# cuenta_corriente.get_saldo() # 0
# monto = input("Ingrese el monto para establecer el saldo: ")
# # if monto.isdigit():
# if cuenta_corriente.validar_monto(monto):
#     monto = float(monto)
#     cuenta_corriente.set_saldo(monto)
#     print("Saldo actualizado:", cuenta_corriente.get_saldo())
# else:
#     print("Por favor, ingrese un monto válido.")

"""
    Practica clase Producto
"""
# nombre = input("Ingrese el nombre del producto: ")
# precio = input("Ingrese el precio del producto: ")
# precio = float(precio)
# producto = Producto(nombre, precio) # instancia de la clase Producto
# precio = producto.get_precio()
# print(f"El precio del producto '{nombre}' es: {precio}")

# precio_nuevo = input("Ingrese el precio nuevo del producto: ")
# precio_nuevo = float(precio_nuevo)
# producto.set_precio(precio_nuevo) # modificar el precio usando el setter
# precio = producto.get_precio()
# print(f"El precio del producto '{nombre}' es: {precio}")

"""
Ejercicio con la clase Empleado:
"""
cantidad_empleados = 3
empleados = []

for i in range(cantidad_empleados):
    print(f"Ingrese los datos del empleado {i+1}:")
    nombre = input(f"Ingrese el nombre del empleado: ")
    salario = input(f"Ingrese el salario del empleado: ")
    salario = float(salario)
    empleado = Empleado(nombre, salario)
    empleados.append(empleado)
    if i > 0:
        aumento = input(f"Ingrese el aumento para el empleado ej 1.30 {empleado.nombre}: ")
        aumento = float(aumento)
        Empleado.modificar_aumento_general(aumento)
    else:
        print("No se aplicará aumento al primer empleado.")

print("\nInformación de los empleados:")
for empleado in empleados:
    print(f"Nombre: {empleado.nombre}, Salario: {empleado.salario}, Salario con aumento: {empleado.salario * Empleado.aumento_general}")
    if Empleado.es_sueldo_alto(empleado.salario):
        print(f"El salario de {empleado.nombre} es alto.")
    else:
        print(f"El salario de {empleado.nombre} es bajo.")

