from .filtros import (
    filtrar_continente,
    filtrar_poblacion,
    filtrar_superficie
)

def menu_filtros(lista_paises):
    """
    Permite al usuario elegir un filtro y utiliza
    la función correspondiente de filtros
    """
    print("¿Con qué criterio desea filtrar?\n1- Continente\n2- Población\n3- Superficie")

    while True:
        try:
            opcion = int(input("Ingrese una opción (1-3): "))
        except ValueError:
            print("Debe ingresar un número entero.")
            continue

        match opcion:
            # Utilizamos match case para las opciones y llamamos a las funciones de filtros.py
            case 1:
                continentes = sorted({p["continente"].title() for p in lista_paises})
                print("Continentes disponibles:", ", ".join(continentes))
    
                while True:
                    continente = input("Ingrese el continente: ")
                    if continente.strip() == "":
                        print("Debe ingresar letras, no puede quedar vacío.")
                    else:
                        break
    
                resultado = filtrar_continente(lista_paises, continente)

            case 2 | 3:
                try:
                    minimo = int(input("Ingrese el mínimo: ").strip())
                    maximo = int(input("Ingrese el máximo: ").strip())
                except ValueError:
                    print("Debe ingresar números enteros.")
                    continue

                try:
                    if opcion == 2:
                        resultado = filtrar_poblacion(lista_paises, minimo, maximo)
                    else:
                        resultado = filtrar_superficie(lista_paises, minimo, maximo)
                except ValueError as e:
                    print(e)
                    continue

            case _:
                print("Opción fuera de rango.")
                continue

        # Mostramos el resultado
        if resultado:
            for pais in resultado:
                print(f"- {pais['nombre'].title()}")
        else:
            print("No se encontraron países con ese criterio.")
        break