def buscar_pais(lista_paises):

    # Pedimos al usuario el nombre del pais a buscar
    buscado = input("Ingrese el nombre del pais a buscar: ").lower().strip()

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