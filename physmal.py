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

# Energía interna de gases ideales

if respuesta_0 == 3:
    from Funciones.energía_interna_gases import *
    energía_interna_gases()
    
# Transformación de lorentz posición

if respuesta_0 == 4:
    from Funciones.transformación_lorentz_posición import *
    transformación_lorentz_posición()

# Transformación de lorentz tiempo

if respuesta_0 == 5:
    from Funciones.transformación_lorentz_tiempo import *
    transformación_lorentz_tiempo()
