
def transformación_lorentz_posición():
    import math
    from Constantes.generales import gene
    x = float(input("\n¿Posición según el que está en reposo?\n"))
    v = float(input("\n¿Velocidad del sistema en movimiento?\n"))
    t = float(input("\n¿Tiempo medido desde el sistema quieto?\n"))
    if v < gene["velocidad luz"]:
        xx = (x - v*t)/(math.sqrt(1-(v/gene["velocidad luz"])**2))
        print(xx)
    else:
        print("\nLa velocidad no puede superar al valor 299792458.\n"
              "Nada viaja más rápido que la luz.\n")
























