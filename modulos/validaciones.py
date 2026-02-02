from modulos.gestion_datos import codigos_registrados


def validar_texto(texto):
    return texto != ""


def validar_precio(precio):
    return precio > 0


def codigo_disponible(codigo):
    return codigo not in codigos_registrados
