def buscar_pais(lista_paises):
    """
    Permite buscar un pais por su nombre.
    Considera coincidencias parciales y
    muestra los datos de las coincidencias.
    """

    # Pedimos al usuario el nombre del pais a buscar
    while True:
        buscado = input("Ingrese el nombre del pais a buscar: ").lower().strip()

        # Verificamos si esta vacío
        if not buscado:
            print("Error: El nombre no puede estar vacío.")
            break

        # Inicializamos la siguiente variable bandera
        encontrado = False

        print(f"\nResultados para: '{buscado}'")
        print("-" * 30)

        for pais in lista_paises:
            if buscado in pais["nombre"].lower():
                print(f"Encontrado: {pais['nombre']} | Población: {pais['poblacion']}")
                print(f"Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
                encontrado = True
                
        if not encontrado:
            print("No se encontraron países que coincidan con ese nombre.")