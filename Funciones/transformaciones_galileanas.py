
def t_galileana():

    v = float(input("\nTienes 2 sistamas A y B, el segundo se mueve a\n"
          "velocidad constante con respecto al primero.\n"
          "Escribe esa velocidad\n"))
    t = float(input('¿Qué tiempo midió el sistema "quieto"?\n'))
    x = float(input('¿Qué posición mide el sistema "quieto"?\n'))
    xx = x - v*t
    print('La posición que mide el sistema en "movimiento" es {}metros\n'.format(str(xx)))
    return xx




















