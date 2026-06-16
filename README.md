# TPI Programación 1

Trabajo Práctico Integrador de la Tecnicatura Universitaria en Programación a Distancia (TuPAD).
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

**Integrantes:**

* Carlos Cejas
* Agustín Atminis

## Documentación

* **Informe PDF:** https://drive.google.com/file/d/1SEBBX5fO91lXny7PUsse2PAuh_Bk9SVV/view?usp=sharing
* **Video de presentación:** 

## Estructura del proyecto

```text
proyecto/
├── datos/
│   └── paises.csv
│
├── funciones/
│   ├── __init__.py
│   ├── actualizar_pais.py
│   ├── agregar_paises.py
│   ├── buscar_pais.py
│   ├── cargar_paises.py
│   ├── filtros.py
│   ├── guardar_paises.py
│   ├── menu_filtros.py
│   ├── menu_principal.py
│   ├── mostrar_estadisticas.py
│   └── ordenar_paises.py
│
├── main.py
└── README.md
```

## Descripción de los módulos

| Archivo                   | Descripción                                         |
| ------------------------- | --------------------------------------------------- |
| `actualizar_pais.py`      | Actualización de población y superficie de un país. |
| `agregar_paises.py`       | Incorporación de nuevos países al dataset.          |
| `buscar_pais.py`          | Búsqueda por nombre exacto o parcial.               |
| `cargar_paises.py`        | Lectura y carga de datos desde el archivo CSV.      |
| `filtros.py`              | Filtrado por continente, población y superficie.    |
| `guardar_paises.py`       | Persistencia de datos en formato CSV.               |
| `menu_filtros.py`         | Menú de opciones de filtrado.                       |
| `menu_principal.py`       | Menú principal de la aplicación.                    |
| `mostrar_estadisticas.py` | Cálculo y visualización de estadísticas generales.  |
| `ordenar_paises.py`       | Ordenamiento de países según distintos criterios.   |
| `main.py`                 | Punto de entrada de la aplicación.                  |

## Dataset

El proyecto incluye un dataset con **25 países previamente cargados**, listos para utilizar con todas las funcionalidades desarrolladas.

Los datos contemplan países de distintos continentes, con diversidad en:

* Población
* Superficie

## Características

* Gestión de países mediante menú interactivo.
* Agregado de nuevos paises con sus datos correspondientes.
* Actualización de datos existentes.
* Búsqueda por nombre (coincidencia parcial o exacta).
* Filtrado por múltiples criterios.
* Ordenamiento de resultados.
* Generación de estadísticas generales.
* Persistencia de datos mediante archivos CSV.

## Aspectos de diseño

El proyecto se encuentra **modularizado**, asignando una única responsabilidad a cada módulo y función.

Además, el código está documentado mediante:

* Comentarios descriptivos.
* Docstrings en funciones.
* Separación clara de responsabilidades.
* Estructura organizada en paquetes y módulos.
