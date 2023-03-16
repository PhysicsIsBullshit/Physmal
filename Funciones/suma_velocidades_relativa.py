
def suma_de_velocidades_relativa():
    import math
    from Constantes.generales import gene
    print("\nTienes 2 sistemas uno se mueve con respecto al otro en el eje x\n"
          "y ambos ven un cuerpo moverse.\n")
    v = int(input("\n¿Cuál es la velocidad de ese sistema?\n"))
    q = int(input("\n¿Qué velocidad quieres calcular?\n"
                  "1. La velocidad del objeto en el eje x' medida por el sistema que se mueve utizando los datos que mide el sistema en reposo.\n"
                  "2. La velocidad del objeto en el eje y' medida por el sistema que se mueve utizando los datos que mide el sistema en reposo.\n"
                  "3. La velocidad del objeto en el eje z' medida por el sistema que se mueve utizando los datos que mide el sistema en reposo.\n"
                  "4. La velocidad del objeto en el eje x medida por el sistema en reposo utizando los datos que mide el sistema que se mueve.\n"
                  "5. La velocidad del objeto en el eje y medida por el sistema en reposo utizando los datos que mide el sistema que se mueve.\n"
                  "6. La velocidad del objeto en el eje z medida por el sistema en reposo utizando los datos que mide el sistema que se mueve.\n"))
    
    if q in [1,2,3]:
        ux = int(input("\nVelocidad en el eje x del objeto medida por el sistema en reposo.\n"))
        if q == 1:
            uxx = (ux - v)/(1 - ux*v/gene["velocidad luz"]**2)
            print(uxx)
        if q == 2:
            uy = int(input("\nVelocidad en el eje y del objeto medida por el sistema en reposo.\n"))
            uyy = uy*math.sqrt(1-(v/gene["velocidad luz"])**2)/(1 - ux*v/gene["velocidad luz"]**2)
            print(uyy)
        if q == 3:
            uz = int(input("\nVelocidad en el eje z del objeto medida por el sistema en reposo.\n"))
            uzz = uz*math.sqrt(1-(v/gene["velocidad luz"])**2)/(1 - ux*v/gene["velocidad luz"]**2)
            print(uzz)

    if q in [4,5,6]:
        uxx = int(input("\nVelocidad en el eje x' del objeto medida por el sistema en movimiento.\n"))
        if q == 4:
            ux = (uxx + v)/(1 + uxx*v/gene["velocidad luz"]**2)
            print(ux)
        if q == 5:
            uyy = int(input("\nVelocidad en el eje y' del objeto medida por el sistema en movimiento.\n"))
            uy = uyy*math.sqrt(1-(v/gene["velocidad luz"])**2)/(1 + uxx*v/gene["velocidad luz"]**2)
            print(uy)
        if q == 6:
            uzz = int(input("\nVelocidad en el eje z' del objeto medida por el sistema en movimiento.\n"))
            uz = uzz*math.sqrt(1-(v/gene["velocidad luz"])**2)/(1 + uxx*v/gene["velocidad luz"]**2)
            print(uz)
















