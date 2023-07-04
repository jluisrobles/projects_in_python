import os
import shutil
from pathlib import Path

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_bienvenida():
    print("¡Bienvenido al programa de recetas!")
    print("-------------------------------")
    print()

def obtener_ruta_recetas():
    ruta_escritorio = Path.home() / "Desktop"
    ruta_recetas = ruta_escritorio / "recetas"
    return ruta_recetas

def mostrar_ruta_recetas(ruta_recetas):
    print(f"La carpeta de recetas se encuentra en: {ruta_recetas}")
    print()

def contar_recetas(ruta_recetas):
    contador = 0
    for archivo in ruta_recetas.iterdir():
        if archivo.is_file():
            contador += 1
    return contador

def mostrar_total_recetas(total_recetas):
    print(f"Total de recetas en la carpeta: {total_recetas}")
    print()

def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Leer receta")
    print("2. Crear nueva receta")
    print("3. Crear nueva categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")
    print()

def seleccionar_opcion():
    opcion = input("Seleccione una opción: ")
    print()
    return opcion

def elegir_categoria(ruta_recetas):
    print("Categorías disponibles:")
    categorias = [item.name for item in ruta_recetas.iterdir() if item.is_dir()]
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")
    print()
    opcion = int(input("Seleccione una categoría: "))
    categoria_elegida = categorias[opcion - 1]
    return categoria_elegida

def leer_receta(ruta_recetas, categoria):
    categoria_path = ruta_recetas / categoria
    recetas = [item.stem for item in categoria_path.iterdir() if item.is_file()]
    print("Recetas disponibles:")
    for i, receta in enumerate(recetas, start=1):
        print(f"{i}. {receta}")
    print()
    opcion = int(input("Seleccione una receta: "))
    receta_elegida = recetas[opcion - 1]
    receta_path = categoria_path / (receta_elegida + ".txt")
    with open(receta_path, "r") as archivo:
        contenido = archivo.read()
        print(f"\n--- Contenido de la receta '{receta_elegida}' ---\n")
        print(contenido)
        print("\n--- Fin de la receta ---\n")

def crear_receta(ruta_recetas, categoria):
    categoria_path = ruta_recetas / categoria
    nombre_receta = input("Ingrese el nombre de la nueva receta: ")
    contenido_receta = input("Ingrese el contenido de la nueva receta: ")
    receta_path = categoria_path / (nombre_receta + ".txt")
    with open(receta_path, "w") as archivo:
        archivo.write(contenido_receta)
    print(f"La receta '{nombre_receta}' se ha creado correctamente en la categoría '{categoria}'.")

def crear_categoria(ruta_recetas):
    nombre_categoria = input("Ingrese el nombre de la nueva categoría: ")
    categoria_path = ruta_recetas