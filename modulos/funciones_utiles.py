import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_titulo(texto):
    print("=" * len(texto))
    print(texto)
    print("=" * len(texto))


def contar_productos(productos, categoria=None):
    if not productos:
        return 0

    # Normalizamos para evitar errores de mayusculas y espacios
    cat_producto = productos[0]["categoria"].strip().lower()
    cat_busqueda = categoria.strip().lower() if categoria else None

    if cat_busqueda is None or cat_producto == cat_busqueda:
        return 1 + contar_productos(productos[1:], categoria)
    else:
        return contar_productos(productos[1:], categoria)