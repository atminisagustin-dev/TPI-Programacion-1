def filtrar_continente(lista_paises, continente):
    """
    Filtra países por continente.
    Retorna lista de países que pertenecen al continente dado
    """
    continente = continente.strip().lower()
    resultado = []

    for pais in lista_paises:
        if pais["continente"].strip().lower() == continente:
            resultado.append(pais)

    if resultado:
        return resultado
    return None


def filtrar_poblacion(lista_paises, minimo, maximo):
    """
    Filtra países cuya población esté entre minimo y maximo.
    Retorna lista de países que se encuentran en ese rango.
    """
    if minimo > maximo:
        raise ValueError(f"El mínimo ({minimo}) no puede ser mayor que el máximo ({maximo}).")

    resultado = []

    for pais in lista_paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultado.append(pais)

    if resultado:
        return resultado
    return None


def filtrar_superficie(lista_paises, minimo, maximo):
    """
    Filtra países cuya superficie esté entre minimo y maximo.
    Retorna lista de países que se encuentren en ese rango.
    """
    if minimo > maximo:
        raise ValueError(f"El mínimo ({minimo}) no puede ser mayor que el máximo ({maximo}).")

    resultado = []

    for pais in lista_paises:
        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)

    if resultado:
        return resultado
    return None