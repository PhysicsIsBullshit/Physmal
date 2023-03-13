
def energía_interna_gases():
    from Constantes.constantes_generales import constantes_generales
    n = int(input("\n¿Número de moles?\n"))
    T = int(input("\n¿Temperatura?\n"))
    U = 1.5*n*T*constantes_generales["gases ideales"]
    print(U)

    





























