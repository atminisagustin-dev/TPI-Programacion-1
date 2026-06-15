# TPI-Programacion-1
Trabajo Practico Integrador TuPAD Programación 1- Carlos Cejas y Agustin Atminis

Link a PDF: https://drive.google.com/file/d/1SEBBX5fO91lXny7PUsse2PAuh_Bk9SVV/view?usp=sharing
Link a video:

Estructura del proyecto:

📦 proyecto
├── 📁 datos
│   └── 📄 paises.csv                # Dataset de paises
│
├── 📁 funciones
│   ├── 📄 __init__.py               # Convierte la carpeta en un paquete
│   ├── 📄 actualizar_pais.py        # Actualización de datos
│   ├── 📄 agregar_paises.py         # Agregar nuevos paises
│   ├── 📄 buscar_pais.py            # Búsqueda por nombre (coincidencia parcial o exacta)
│   ├── 📄 cargar_paises.py          # Convierte los datos del dataset en una lista de dicts
│   ├── 📄 filtros.py                # Filtros por continente, población y superficie
│   ├── 📄 guardar_paises.py         # Escritura en CSV
│   ├── 📄 menu_filtros.py           # Menú de filtrado
│   ├── 📄 menu_principal.py         # Menú principal
│   ├── 📄 mostrar_estadisticas.py   # Estadísticas generales
│   └── 📄 ordenar_paises.py         # Ordenamiento de datos
│
├── 📄 main.py                       # Punto de entrada de la aplicación
└── 📄 README.md                     # Documentación del proyecto

El proyecto incluye un dataset con 25 paises previamente cargados listos para utilizar
con las funciones creadas. Se proveen cinco paises de cada continente con gran diversidad
en población y superficie.

El proyecto se encuentra modularizado otorgando una sola responsabilidad a cada función. Se
encuentra documentada a traves de comentarios y docstrings en las funciones.