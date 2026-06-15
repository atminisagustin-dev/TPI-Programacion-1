from funciones import (
    menu_principal,
    actualizar_pais,
    agregar_paises,
    buscar_pais,
    cargar_paises,
    menu_filtros,
    mostrar_estadisticas,
    ordenar_paises,
    guardar_paises
)

ARCHIVO_CSV = "datos/paises.csv"

print("Cargando datos...")
lista_paises = cargar_paises(ARCHIVO_CSV)

if lista_paises:
    print(f"Se han cargado {len(lista_paises)} paises correctamente.")
else:
    print("No se han cargado paises")

while True:
    menu_principal()

    try:
        opciones = int(input("Elija una opcion: "))
    except ValueError:
        print("Debe ingresar un numero entero.")
        continue
    else:
        match opciones:
            case 1:
                agregar_paises(lista_paises)
                guardar_paises(ARCHIVO_CSV,lista_paises)
            case 2:
                actualizar_pais(lista_paises)
                guardar_paises(ARCHIVO_CSV, lista_paises)
            case 3:
                buscar_pais(lista_paises)
            case 4:
                menu_filtros(lista_paises)
            case 5:
                ordenar_paises(lista_paises)
            case 6:
                mostrar_estadisticas(lista_paises)
            case 7:
                guardar_paises(ARCHIVO_CSV, lista_paises)
                print("Archivo guardado con exito.")
                break
            case _:
                print("Opción fuera de rango.")