## Script de interacción con el usuario para el uso del programa physmal.


# Temas disponibles.
temas = [
    "Tranformaciones de Lorentz",
    "Transformaciones inversas de lorentz",
    "Dilatación del tiempo",
    "Contracción de la longitud",
    "Pitágoras",
    "Dispersión de Compton",
    "Líneas espectrales"
    ]

temas.sort() # Ordena los temas alfabéticamente

# Interacción con el usuario.

print("Bienvenido a Physmal.\nEscriba el número correspondiente:")

respuesta_0 = input("""
1. Escribir problema.
2. Mostrar los problemas disponibles.
""")

if respuesta_0 == "1":
    respuesta_1 = input("""
    ¿Qué es lo que quieres resolver?
    """)

    if respuesta_1 == "pitagoras":
        from Funciones.Generales.pitágoras import *
        print(pitagoras(*input_pit()))

elif respuesta_0 == "2":
    print("-----------------------------")
    for tema in temas:
        print(tema)
    print("-----------------------------")
