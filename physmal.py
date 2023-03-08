## Comentario



funciones_rel_esp = ["dilatación", "contracción"]


# Interacción con el usuario.

print("Bienvenido a Physmal.")
respuesta_1 = input("""
¿Qué es lo que quieres resolver?
""")


if respuesta_1 == "pitagoras":
    from Funciones.Generales.pitágoras import *
    print(pitagoras(*input_pit()))

    


# respuesta_2 = int(input("""
# 1. dilataciónpigh
# 2. contracción
# """))