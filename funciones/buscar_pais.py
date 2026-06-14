import csv

def buscar_pais(nombre_archivo):

    # Pedimos al usuario el nombre del pais a buscar
    buscado = input("Ingrese el nombre del pais a buscar: ").lower().strip()

    # Inicializamos la siguiente variable bandera
    encontrado = False

    # Validamos que exista el archivo .csv
    try:
        # Abrimos el archivo .csv para lectura
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            # Converrtimos cada fila en un diccionario
            reader = csv.DictReader(archivo)
            
            print(f"\nResultados para: '{buscado}'")
            print("-" * 30)

            for fila in reader:
                if buscado in fila["nombre"].lower():
                    print(f"Encontrado: {fila['nombre']} | Población: {fila['poblacion']}")
                    print(f"Superficie: {fila['superficie']} km² | Continente: {fila['continente']}")
                    encontrado = True
            
            if not encontrado:
                print("No se encontraron países que coincidan con ese nombre.")

    except FileNotFoundError:
        print("Error: El archivo no existe.")