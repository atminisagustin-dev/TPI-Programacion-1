def filtrar_paises(lista_paises):
    """
    Permite filtrar los paises de la lista segun continente,
    rango de población o rango de superficie
    """
    print("¿Con que criterio desea filtrar los paises?\n1-Continente\n2-Rango de población\n3- Rango de superficie")
    opcion = input("Ingrese una opción (1-3): ")

    while True:
        try:
            opcion = int(opcion)
        except ValueError:
            print("Debe ingresar un numero.")
            return
        else:
            match opcion:
                case 1:
                    continentes = []

                    for pais in lista_paises:
                        continente = pais["continente"]

                        if continente not in continentes:
                            continentes.append(continente)
                    
                    continentes.sort()

                    print("Continentes disponibles: ", *continentes, sep= ", ")

                    paises_continente = input("Ingrese el continente: ").strip().lower()

                    resultado = []

                    for pais in lista_paises:
                        if pais["continente"].lower() == paises_continente.lower():
                            resultado.append(pais)
                    
                    if resultado:
                        print(f"Paises en {paises_continente}: ")
                        for pais in resultado:
                            print(f"- {pais['nombre']}")
                        break
                    
                    else:
                        print("No se encontro un continente con ese nombre.")
                        break

                case 2:
                    try:
                        minimo = int(input("Ingrese la población minima: ").strip())
                        maximo = int(input("Ingrese la población maxima: ").strip())
                    except ValueError:
                        print("Debe ingresar numeros enteros.")
                    else:
                        resultado = []

                        for pais in lista_paises:
                            if pais['poblacion'] >= minimo and pais['poblacion'] <= maximo:
                                resultado.append(pais)
                        
                        if resultado:
                            print(f"Paises con población entre {minimo} y {maximo}: ")
                            for pais in resultado:
                                print(f"- {pais['nombre']}: {pais['poblacion']} habitantes.")
                            break
                        
                        else:
                            print("No se encontraron paises en ese rango.")
                            break

                case 3:
                    try:
                        minimo = int(input("Ingrese la superficie minima (km²): ").strip())
                        maximo = int(input("Ingrese la superficie maxima (km²): ").strip())
                    except ValueError:
                        print("Debe ingresar numeros enteros.")
                    else:
                        resultado = []

                        for pais in lista_paises:
                            if pais['superficie'] >= minimo and pais['superficie'] <= maximo:
                                resultado.append(pais)
                        
                        if resultado:
                            print(f"Paises con superficie entre {minimo} y {maximo}: ")
                            for pais in resultado:                        
                                print(f"- {pais['nombre']}: {pais['superficie']} km².")
                            break
                        else:
                            print("No se encontraron paises en ese rango.")
                            break
                case _:
                    print("Opcion fuera de rango.")
                    break