from modulos.datos_basicos import cargar_producto
from modulos.gestion_datos import (
    agregar_producto,
    listar_productos,
    eliminar_producto_por_id,
    productos
)
from modulos.funciones_utiles import (
    imprimir_titulo, 
    contar_productos,
    limpiar_pantalla
)


def ejecutar_menu():
    while True:
        imprimir_titulo("MENU PRINCIPAL")

        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Eliminar producto")
        print("4. Contar productos")
        print("5. Limpiar pantalla")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            producto = cargar_producto()
            agregar_producto(producto)

        elif opcion == "2":
            listar_productos()

        elif opcion == "3":
            producto_id = int(input("Ingrese ID a eliminar: "))
            if eliminar_producto_por_id(producto_id):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            total = contar_productos(productos)
            print(f"Total de productos: {total}")

        elif opcion == "5":
            limpiar_pantalla()
            continue 

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opcion invalida.")
            continue
