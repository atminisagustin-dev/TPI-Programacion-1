import csv

# Creamos la lista para mostrar resultados
lista_paises = []

def ordenar_paises(nombre_archivo):

    # Intentamos abrir el archivo .csv
    try:
        # Abrimos en solo lectura
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                # Convertimos los valores a numericos para que el orden sea el correcto
                fila['poblacion'] = int(fila['poblacion'])
                fila['superficie'] = int(fila['superficie'])
                lista_paises.append(fila)

    # Salimos si no hay archivo .csv
    except FileNotFoundError:
        print("Error: El archivo no esiste.")
        return
    
    # Pedimos al usuario una opción
    opcion = input("""\n¿Porque Campo desea ordenar?
                1) Nombre
                2) Población
                3) Superficie
                    Seleccione una Opción (1-3): """)
    
    # Creamos un diccionario para luego acceder al campo elegido
    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}

    # Validamos entrada del usuario
    if opcion not in campos:
        print("Error: Opción invalida.")
        return
    
    # Extraemos campo seleccionado y lo guardamos en la siguiente variable
    clave_orden = campos[opcion]

    # Pedimos al usuario que ingrese el orden en el que desea ordenar los campos
    orden = input("¿Orden Ascendente? s/n").lower().strip()

    # Creamos una variable con un valor booleano
    reverse = True if orden == "s" else False

    # Utilizamos sort() para ordenar la lista, y una función lambda para acceder al campo elegido
    # Utilizamos la variable booleana reverse para corregir el orden ya sea ascendente o descendente
    lista_paises.sort(key=lambda x: x[clave_orden], reverse=not reverse)

    # Imprimimos por pantalla el siguiente mensaje
    print(f"\nResultados ordenados por {clave_orden}:")

    # Recorremos la lista e imprimimos por pantalla los resultados 
    for p in lista_paises:
        print(f"{p['nombre']} | Pob: {p['poblacion']} | Sup: {p['superficie']} km² | Cont: {p['continente']}")