import csv

def guardar_paises(nombre_archivo, lista_paises):
    with open(nombre_archivo, mode="w", encoding='utf-8', newline="") as archivo:

        # Establecemos el orden con el que se debe agregar los elementos
        campos = ["nombre", "poblacion", "superficie", "continente"]

        # Creamos el objeto escritor
        writer = csv.DictWriter(archivo, fieldnames=campos)

        # Agregamos a lista de diccionarios
        writer.writeheader()
        writer.writerows(lista_paises)