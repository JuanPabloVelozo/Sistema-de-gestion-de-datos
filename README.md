# Sistema de Gestión de Productos

Proyecto desarrollado en Python para gestionar productos desde consola, aplicando estructuras de control, funciones, estructuras de datos y modularización.

## Funcionalidades
- Agregar productos con validación de datos.
- Listar productos registrados.
- Eliminar productos por ID.
- Contar la cantidad total de productos.
- Limpiar la pantalla de la consola.
- Menú interactivo para la gestión del sistema.

## Funcionamiento
El sistema se ejecuta desde consola y permite administrar productos mediante un menú principal.  
Los productos se almacenan como diccionarios dentro de una lista y se validan los datos ingresados para evitar errores y duplicados.

## Variables principales
- `productos`: lista de productos.
- `codigos_registrados`: conjunto para evitar códigos duplicados.
- `categirias`: tupla de categorías disponibles.
- `_id_actual`: generador de IDs incrementales.

## Estructura del proyecto
/main.py
/modulos/init.py
/modulos/menu.py
/modulos/gestion_datos.py
/modulos/datos_basicos.py
/modulos/validaciones.py
/modulos/funciones_utiles.py
README.md

## Tecnologías
- Python 3
- Visual Studio Code

## Ejecución
Ejecutar el archivo `main.py` desde la terminal:

```bash
python main.py
