import csv

def agregar_paises(nombre_archivo):

    # Abrimos un bloque Try para validar entradas
    try:
        # Pedimos al usuario la cantidad de paises a agregar
        cantidad_paises = int(input("Ingrese la cantidad de paises a agregar: "))
    except ValueError:
        print("Error: Ingrese un Número valido: ")
        return
    
    # Creamos una lista de diccionarios
    lista_paises = []

    # Inicializamos un ciclo For para pedir la cantidad de paises ingresada por el usuario
    for i in range(cantidad_paises):
        print(f"Pais {i+1}/{cantidad_paises+1}:")
        nombre = input("Ingrese Nombre: ")

        # Inicializamos un ciclo while para validar entradas del usuario
        while True:
            try:
                poblacion = int(input("Población: "))
                superficie = int(input("Superficie (km2): "))
                break
            except ValueError:
                print("Error: Debes ingresar números enteros para población y superficie. Intenta de nuevo.")

        continente = input("Continente: ")

        # Creamos el diccionario con los valores ingresados
        pais = {
            "nombre" : nombre,
            "poblacion" : poblacion,
            "superficie" : superficie,
            "continente" : continente
        }

        # Agregamos a la lista el diccionario
        lista_paises.append(pais)

    # Abrimos el bloque with para trabajar con el archivo .csv
    with open(nombre_archivo, "a", newline='', encoding='utf-8') as archivo:

        # Establecemos el orden con el que se debe agregar los elementos
        campos = ["nombre", "poblacion", "superficie", "continente"]

        # Creamos el objeto escritor
        writer = csv.DictWriter(archivo, fieldnames=campos)

        # Agregamos a lista de diccionarios
        writer.writerows(lista_paises)

    # Informamos al usuario el exito de la operación
    print(f"\n¡Se han añadido {cantidad_paises} países exitosamente al archivo '{nombre_archivo}'!")