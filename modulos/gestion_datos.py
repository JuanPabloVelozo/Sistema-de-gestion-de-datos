# LISTA de productos
productos = []

# SET para evitar codigos duplicados
codigos_registrados = set()

# TUPLA inmutable de categorias
CATEGORIAS = ("Electronica", "Alimentos", "Ropa", "Hogar")

# ID incremental
_id_actual = 0


def generar_id():
    global _id_actual
    _id_actual += 1
    return _id_actual


def agregar_producto(producto):
    productos.append(producto)
    codigos_registrados.add(producto["codigo"])


def listar_productos():
    if not productos:
        print("No hay productos cargados.")
        return

    for p in productos:
        print(
            f"ID: {p['id']} | "
            f"Codigo: {p['codigo']} | "
            f"Nombre: {p['nombre']} | "
            f"Precio: ${p['precio']} | "
            f"Categoria: {p['categoria']}"
        )


def buscar_producto_por_codigo(codigo):
    for p in productos:
        if p["codigo"] == codigo:
            return p
    return None


def eliminar_producto_por_id(producto_id):
    for p in productos:
        if p["id"] == producto_id:
            productos.remove(p)
            codigos_registrados.remove(p["codigo"])
            return True
    return False

