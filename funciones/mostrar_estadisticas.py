def mostrar_estadisticas(lista_paises):
    """
    Calcula y muestra estadísticas del dataset:
    - País con mayor y menor población
    - Promedio de población
    - Promedio de superficie
    - Cantidad de países por continente
    """

    print("--- ESTADÍSTICAS ---\n")

    mayor_pob = lista_paises[0]
    menor_pob = lista_paises[0]
    total_pob = 0
    total_sup = 0
    conteo = {}

    for pais in lista_paises:
        # Mayor y menor población
        if pais["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = pais
        if pais["poblacion"] < menor_pob["poblacion"]:
            menor_pob = pais

        # Acumuladores para promedios
        total_pob += pais["poblacion"]
        total_sup += pais["superficie"]

        # Conteo por continente
        c = pais["continente"]
        if c in conteo:
            conteo[c] += 1
        else:
            conteo[c] = 1

    promedio_pob = total_pob // len(lista_paises)
    promedio_sup = total_sup // len(lista_paises)

    print(f"  Total de países cargados : {len(lista_paises)}")
    print()
    print(f"  País con mayor población : {mayor_pob['nombre'].title()} - ({mayor_pob['poblacion']} hab.)")
    print(f"  País con MENOR población : {menor_pob['nombre'].title()} - ({menor_pob['poblacion']} hab.)")
    print(f"  Promedio de población    : {promedio_pob} hab.")
    print()
    print(f"  Promedio de superficie   : {promedio_sup} km²")
    print()

    print("  Países por continente:")
    for continente in sorted(conteo):
        print(f"    {continente.title()} : {conteo[continente]} paises")
