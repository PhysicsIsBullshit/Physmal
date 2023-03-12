## Script de interacción con el usuario para el uso del programa physmal.

# Interacción con el usuario.

respuesta_0 = int(input("Bienvenido a Physmal.\nEscribir el número asociado al problema:"))

# Pitágoras

if respuesta_0 == 1:
    from Funciones.Generales.pitágoras import *
    print(pitagoras(*input_pit()))

# Transformación galileana posición

if respuesta_0 == 2:
    from Funciones.transformaciones_galileanas import *
    t_galileana()
