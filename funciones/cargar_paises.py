import csv

def cargar_paises(nombre_archivo):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios
    Cada diccionario contiene un pais y sus datos de
    población, superficie y continente
    """
    # Crea una lista vacia donde se almacenaran los diccionarios
    lista_paises = []

    try:
        with open(nombre_archivo, mode='r', encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                # Recorre las filas del dataser y convierte los valores en values de un diccionario
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip()
                    }
                    lista_paises.append(pais)
                except ValueError:
                    print(f"Formato invalido en la fila {fila}.")
    
    except FileNotFoundError:
        print(f"No se ha encontrado el archivo '{nombre_archivo}'")

    return lista_paises