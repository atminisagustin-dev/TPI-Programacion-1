def ordenar_paises(lista_paises):
    """
    Permite ordenar los paises de la lista bajo
    los siguientes criterios:
    - Nombre (ascendente/descendente)
    - Población (ascendente/descendente)
    - Superficie (ascendente/descendente)
    """
    # Pedimos al usuario una opción
    opcion = input("\n¿Por que campo desea ordenar?\n" \
                   "1) Nombre\n" \
                   "2) Población\n" \
                   "3) Superficie\n" \
                   "Seleccione una Opción (1-3): ")
    
    # Creamos un diccionario para luego acceder al campo elegido
    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}

    # Validamos entrada del usuario
    if opcion not in campos:
        print("Error: Opción invalida.")
        return
    
    # Extraemos campo seleccionado y lo guardamos en la siguiente variable
    clave_orden = campos[opcion]

    # Pedimos al usuario que ingrese el orden en el que desea ordenar los campos
    orden = input("¿Orden Ascendente? s/n: ").lower().strip()

    # Creamos una variable con un valor booleano
    reverse = True if orden == "s" else False

    # Utilizamos sorted() para crear una lista ordenada, y una función lambda para acceder al campo elegido
    # Utilizamos la variable booleana reverse para corregir el orden ya sea ascendente o descendente
    # Esto no modifica la lista original
    lista_temporal = sorted(lista_paises, key=lambda x: x[clave_orden], reverse=not reverse)

    # Imprimimos por pantalla el siguiente mensaje
    print(f"\nResultados ordenados por {clave_orden}:")

    # Recorremos la lista e imprimimos por pantalla los resultados 
    for p in lista_temporal:
        print(f"{p['nombre'].title():<15} | Pob: {p['poblacion']:<10} | Sup: {p['superficie']:<10} km² | Cont: {p['continente'].title()}")