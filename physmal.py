## Comentario



funciones_rel_esp = ["dilatación", "contracción"]


# Interacción con el usuario.

print("Bienvenido a Physmal.")
respuesta_1 = input("""
¿Qué es lo que quieres resolver?
""")

# Filtro a minúscula, eliminador de tildes

respuesta_1 = respuesta_1.lower()
filtro_1 = [("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u")]
for i,j in filtro_1:
    respuesta_1 = respuesta_1.replace(i,j)



if respuesta_1 == "pitagoras":
    from Funciones.Generales.pitágoras import *
    print(pitagoras(*input_pit()))

    


# respuesta_2 = int(input("""
# 1. dilataciónpigh
# 2. contracción
# """))