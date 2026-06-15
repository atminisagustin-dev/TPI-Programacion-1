import csv

def agregar_paises(nombre_archivo, lista_paises):

    # Abrimos un bloque Try para validar entradas
    try:
        # Pedimos al usuario la cantidad de paises a agregar
        cantidad_paises = int(input("Ingrese la cantidad de paises a agregar: "))
    except ValueError:
        print("Error: Ingrese un Número valido: ")
        return
    
    # Creamos una lista de diccionarios
    nuevos_paises = []

    # Inicializamos un ciclo For para pedir la cantidad de paises ingresada por el usuario
    for i in range(cantidad_paises):
        print(f"Pais {i+1}/{cantidad_paises}:")
        while True:
            nombre = input("Ingrese Nombre: ").lower().strip()
            
            # Verificamos si está vacío
            if not nombre:
                print("Error: El nombre no puede estar vacío.")
                continue
                
            # Verificamos si ya existe en la lista (comparando nombres)
            # any() es una forma eficiente de buscar en una lista
            existe = any(pais["nombre"].lower() == nombre for pais in lista_paises)
            
            if existe:
                print(f"Error: El país '{nombre}' ya se encuentra en la base de datos.")
            else:
                break # El nombre es válido y no existe, salimos del while
        
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
        nuevos_paises.append(pais)

    # Actualizar la lista en memoria
    lista_paises.extend(nuevos_paises)

    # Informamos al usuario el exito de la operación
    print(f"\n¡Se han añadido {cantidad_paises} países exitosamente al archivo '{nombre_archivo}'!")