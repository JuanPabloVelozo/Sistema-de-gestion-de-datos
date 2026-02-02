import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_titulo(texto):
    print("=" * len(texto))
    print(texto)
    print("=" * len(texto))


def contar_productos(productos):
    if not productos:
        return 0
    return 1 + contar_productos(productos[1:])

