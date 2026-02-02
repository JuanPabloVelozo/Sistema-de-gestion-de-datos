from modulos.gestion_datos import CATEGORIAS, generar_id
from modulos.validaciones import validar_texto, validar_precio, codigo_disponible


def cargar_producto():
    producto = {}

    producto["id"] = generar_id()

    # Codigo
    codigo = input("Codigo del producto: ").strip()
    while not validar_texto(codigo) or not codigo_disponible(codigo):
        print("Codigo invalido o duplicado.")
        codigo = input("Codigo del producto: ").strip()
    producto["codigo"] = codigo

    # Nombre
    nombre = input("Nombre del producto: ").strip()
    while not validar_texto(nombre):
        print("Nombre invalido.")
        nombre = input("Nombre del producto: ").strip()
    producto["nombre"] = nombre

    # Precio (VALIDADO)
    while True:
        try:
            precio = float(input("Precio: "))
            if validar_precio(precio):
                producto["precio"] = precio
                break
            else:
                print("Precio invalido. Debe ser mayor a 0.")
        except ValueError:
            print("Error: ingrese un numero valido.")

    # Categoria (VALIDADA)
    print("Categorias disponibles:")
    for i, cat in enumerate(CATEGORIAS, start=1):
        print(f"{i}. {cat}")

    while True:
        try:
            opcion = int(input("Seleccione categoria: "))
            if 1 <= opcion <= len(CATEGORIAS):
                producto["categoria"] = CATEGORIAS[opcion - 1]
                break
            else:
                print("Opcion fuera de rango.")
        except ValueError:
            print("Error: debe ingresar un numero.")
    print("Se completo el registro del producto")
    return producto
