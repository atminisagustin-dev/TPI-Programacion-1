def actualizar_pais(lista_paises):
    """
    Permiter actualizar la población y superficie de un pais.
    """
    nombre_buscado = input("Ingrese el nombre del pais a actualizar: ").lower().strip()

    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscado:
            print(f"{pais['nombre']} ha sido encontrado correctamente.")

            while True:
                entrada = input(f"La población actual de {pais['nombre']} es {pais['poblacion']}. ¿Desea cambiarla?(Presione enter para no cambiar) ")
                # Preguntamos si se quiere cambiar la población y damos la opción de no cambiarla
                if entrada == "":
                    break
                try:
                    nueva_poblacion = int(entrada)
                except ValueError:
                    print("Debe ingresar un numero valido.")
                else:
                    if nueva_poblacion > 0:
                        pais["poblacion"] = nueva_poblacion
                        break
                    else:
                        print("Debe ingresar un numero mayor a cero")
            
            while True: 
                entrada = input(f"La superficie actual de {pais['nombre']} es {pais['superficie']} km². ¿Desea cambiarla?(Presione enter para no cambiar) ")
                # Preguntamos si se quiere cambiar la superficie y damos la opción de no cambiarla
                if entrada == "":
                    break
                try:
                    nueva_superficie = int(entrada)
                except ValueError:
                    print("Debe ingresar un numero valido.")
                else:
                    if nueva_superficie > 0:
                        pais["superficie"] = nueva_superficie
                        break
                    else:
                        print("Debe ingresar un numero mayor a cero.")
            
            print(f"Los datos de {pais['nombre']} fueron actualizados correctamente.")
            return
        
    print(f"El pais {nombre_buscado} no se encuentra en la lista.")

                        

