
def energía_interna_gases():
    from Constantes.generales import gene
    n = int(input("\n¿Número de moles?\n"))
    T = int(input("\n¿Temperatura?\n"))
    U = 1.5*n*T*gene["gases ideales"]
    print(U)

    





























