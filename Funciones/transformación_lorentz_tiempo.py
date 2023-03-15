def transformación_lorentz_tiempo():
    import math
    from Constantes.generales import gene
    x = int(input("\n¿Posición según el que está en reposo?\n"))
    v = int(input("\n¿Velocidad del sistema en movimiento?\n"))
    t = int(input("\n¿Tiempo medido desde el sistema quieto?\n"))
    if v < gene["velocidad luz"]:
        tt = (t-v*x/gene["velocidad luz"]**2)/(math.sqrt(1-(v/gene["velocidad luz"])**2))
        print(tt)
    else:
        print("\nLa velocidad no puede superar al valor 299792458.\n"
              "Nada viaja más rápido que la luz.\n")


