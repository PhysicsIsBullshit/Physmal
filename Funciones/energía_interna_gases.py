
def energía_interna_gases():
    from Constantes.generales import gene
    n = float(input("\n¿Número de moles?\n"))
    T = float(input("\n¿Temperatura?\n"))
    U = 1.5*n*T*gene["gases ideales"]
    print(U)

    





























