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


# Dilatación del tiempo

if respuesta_0 == 6:
    from Funciones.FísicaModerna.dilatación_tiempo import input_dilatación_tiempo
    input_dilatación_tiempo()
    

# Contracción de la longitud

if respuesta_0 == 7:
    from Funciones.FísicaModerna.contracción_longitud import input_contracción_longitud
    input_contracción_longitud()